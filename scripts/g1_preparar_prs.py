#!/usr/bin/env python3
"""Montagem auditável das entradas de PRs para M1.4.1, M1.4.3 e M1.5.3.

Lê exclusivamente arquivos JSON brutos obtidos com gh api (sem acesso à rede).
O campo excluir sempre exige revisão humana; não exclui PRs por heurística.
"""
from __future__ import annotations
import argparse,json,re
from datetime import datetime,timezone
from pathlib import Path

def read(path):return json.loads(Path(path).read_text(encoding='utf-8'))
def flat(p):
    if isinstance(p,list):return [x for a in p for x in (a if isinstance(a,list) else [a])]
    return [p]
def items(p,key):return [i for page in flat(p) for i in page.get(key,[])]
def before(a,b):
    try:return datetime.fromisoformat(a.replace('Z','+00:00')) < datetime.fromisoformat(b.replace('Z','+00:00'))
    except Exception:return False

def main():
    x=argparse.ArgumentParser();x.add_argument('--pasta-brutos',required=True);x.add_argument('--out',required=True);a=x.parse_args()
    root=Path(a.pasta_brutos); ns=root/'prs'/'numeros.txt'
    ids=[int(t.strip()) for t in ns.read_text().splitlines() if t.strip()]
    if not ids:raise SystemExit('Sem PRs. Confira o arquivo prs/numeros.txt')
    rs=[]
    for n in ids:
        detail=read(root/'prs'/f'pr-{n}.json')
        files=flat(read(root/'prs'/f'pr-{n}-files.json'))
        if not all(isinstance(f,dict) and 'filename' in f for f in files):raise ValueError(f'Arquivos de PR {n} incompletos')
        merged=detail.get('merged_at'); sha=(detail.get('head') or {}).get('sha')
        if not merged or not sha:raise ValueError(f'PR {n} sem merged_at ou head.sha')
        if not ('2026-04-18' <= merged[:10] <= '2026-10-18'):raise ValueError(f'PR {n} fora da janela')
        if (detail.get('base') or {}).get('ref')!='master':raise ValueError(f'PR {n} não tem base master')
        rawruns=root/'prs'/f'pr-{n}-runs.json'
        status='sem_evidencia';observacoes=[];step_evidence=[]
        if rawruns.exists():
            runs=[r for r in items(read(rawruns),'workflow_runs') if r.get('head_sha')==sha and r.get('event')=='pull_request']
            observed=False
            for r in runs:
                path=root/'prs'/f'pr-{n}-run-{r["id"]}-jobs.json'
                if not path.exists():
                    observacoes.append(f'Run {r["id"]} sem jobs');continue
                jobs=items(read(path),'jobs');
                if not jobs:
                    observacoes.append(f'Run {r["id"]} sem lista de jobs');continue
                for job in jobs:
                    if not isinstance(job.get('steps'),list):continue
                    observed=True
                    for st in job['steps']:
                        if st.get('name')=='Test Coverage':
                            ok=st.get('conclusion') in ('success','failure') and before(st.get('completed_at') or '',merged)
                            step_evidence.append({'run':r['id'],'job':job.get('id'),'conclusao':st.get('conclusion'),'termino':st.get('completed_at'),'antes_do_merge':ok})
            if any(e['antes_do_merge'] for e in step_evidence):status='executado'
            elif observed:status='nao_executado'
        rs.append({'number':n,'title':detail.get('title'),'author':(detail.get('user') or {}).get('login'),'merged_at':merged,'head_sha':sha,'excluir':None,'justificativa_exclusao':'','files':files,'ci_status':status,'evidencia_ci':step_evidence,'observacoes_ci':observacoes})
    target=Path(a.out);target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(json.dumps(rs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'PRs preparados: {len(rs)}. Revisar excluir para TODOS; conferir evidência CI, renomeações e anexar justificativas antes de consolidar.')

if __name__=='__main__':main()
