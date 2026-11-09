#!/usr/bin/env python3
"""Transformações reprodutíveis de G1 (#98); sem mudanças no Git ou acessos à rede.

Executar na raiz do repositório da equipe. Entradas brutas geradas pelas instruções
no documento e pelo Excalidraw fixado em e1b7aac. Não atribui pontuação.
"""
from __future__ import annotations
import argparse, csv, json, re, statistics, sys
from collections import defaultdict
from pathlib import Path

PACOTES_BASE = {"common", "element", "fractional-indexing", "laser-pointer", "math", "utils"}
EXCLUIR = {"tests", "__snapshots__", "node_modules", "dev-docs", "examples", "dist", "build"}


def jread(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def jout(path, obj):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def rows(path, items, fields):
    path = Path(path); path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(items)


def norm(s):
    return str(s).replace("\\", "/").lstrip("./")


def pacote(s):
    p = norm(s).split("/")
    if len(p)>2 and p[0] == "packages": return p[1]
    if len(p)>1 and p[0] == "excalidraw-app": return "excalidraw-app"
    return None


def prod(s):
    p = norm(s).split("/")
    if not pacote(s) or not (s.endswith(".ts") or s.endswith(".tsx")):
        return False
    if s.endswith(".d.ts") or s.endswith(".test.ts") or s.endswith(".test.tsx"):
        return False
    if any(x in EXCLUIR for x in p): return False
    return True


def test(s):
    s = norm(s)
    return s.startswith("packages/") and (s.endswith(".test.ts") or s.endswith(".test.tsx"))


def inventario(args):
    root = Path(args.src).resolve()
    if not (root / "packages").exists() or not (root / "excalidraw-app").exists():
        raise SystemExit("Erro: --src deve apontar para a raiz do Excalidraw avaliado")
    items = [p.relative_to(root).as_posix() for base in (root/"packages",root/"excalidraw-app") for p in base.rglob("*") if p.is_file()]
    manifest = {"producao": sorted(x for x in items if prod(x)), "testes": sorted(x for x in items if test(x)), "pacotes": sorted({pacote(x) for x in items if prod(x)})}
    if len(manifest["producao"])<20: raise SystemExit("Inventário pequeno demais; confira --src")
    jout(args.out, manifest)
    print(f"Inventário: {len(manifest['producao'])} arquivos de produção; {len(manifest['testes'])} suítes; {len(manifest['pacotes'])} pacotes.")


def alcance(edges, start):
    seen=set(); todo=list(edges.get(start, []))
    while todo:
        p=todo.pop()
        if p in seen: continue
        seen.add(p); todo.extend(edges.get(p,[]))
    return seen


def grafo(args):
    inv=jread(args.inventario); raw=jread(args.grafo)
    all_prod=set(inv["producao"]); graph={}
    if not isinstance(raw, dict): raise SystemExit("Grafo precisa ser dicionário JSON do Madge")
    for source, dests in raw.items():
        s=norm(source)
        if s in all_prod:
            graph[s]=[norm(d) for d in dests if norm(d) in all_prod]
    coverage=len(graph)/len(all_prod)
    if coverage<0.8: raise SystemExit(f"Grafo cobre só {coverage:.1%} dos arquivos de produção. Verifique --basedir e aliases; não use resultado incompleto.")
    edges=defaultdict(set)
    invalid=[]
    for source,dests in graph.items():
        a=pacote(source)
        for d in dests:
            b=pacote(d)
            if a!=b:
                edges[a].add(b)
                if (a in PACOTES_BASE and b=="excalidraw") or (a!="excalidraw-app" and b=="excalidraw-app"):
                    invalid.append({"origem":source,"destino":d,"pacote_origem":a,"pacote_destino":b})
    ps=sorted(inv["pacotes"])
    cycles=[(a,b) for i,a in enumerate(ps) for b in ps[i+1:] if b in alcance(edges,a) and a in alcance(edges,b)]
    scored=[]
    for p in ps:
        ca=sum(p in ds for ds in edges.values()); ce=len(edges[p]); den=ca+ce
        scored.append({"pacote":p,"Ca":ca,"Ce":ce,"I":round(ce/den,6) if den else None,"sem_arestas":den==0})
    out=Path(args.saida)
    jout(out/"M1.1.1-pares-ciclicos.json",{"total_pares":len(cycles),"pares":cycles,"cobertura_grafo":coverage})
    rows(out/"M1.1.2-violacoes.csv",sorted(invalid,key=lambda x:(x["origem"],x["destino"])),["origem","destino","pacote_origem","pacote_destino"])
    rows(out/"M1.1.3-acoplamento.csv",scored,["pacote","Ca","Ce","I","sem_arestas"])
    jout(out/"grafo-pacotes.json",{k:sorted(v) for k,v in edges.items()})
    print(f"Grafo: {len(cycles)} pares cíclicos, {len(invalid)} importações irregulares; {coverage:.0%} inventariado.")


def navegador(args):
    inv=jread(args.inventario); raw=jread(args.grafo); a=jread(args.diretos)
    graph={norm(k):[norm(d) for d in ds] for k,ds in raw.items()}
    direct={norm(x) for x in (a["diretos"] if isinstance(a,dict) else a)}
    all_prod=set(inv["producao"])
    if not direct <= all_prod: raise SystemExit("Arquivos marcados diretamente não constam no inventário: "+str(sorted(direct-all_prod)[:4]))
    data=[]
    for p in sorted(PACOTES_BASE):
        files=sorted(x for x in all_prod if pacote(x)==p)
        for f in files:
            reachable=alcance(graph,f)
            if f in direct or reachable & direct:
                data.append({"pacote":p,"arquivo":f,"classe":"direta" if f in direct else "transitiva", "exemplo_alcancado":f if f in direct else sorted(reachable & direct)[0]})
    resumo={p:{"arquivos_total":sum(pacote(f)==p for f in all_prod),"diretas":sum(r["pacote"]==p and r["classe"]=="direta" for r in data),"transitivas_apenas":sum(r["pacote"]==p and r["classe"]=="transitiva" for r in data)} for p in sorted(PACOTES_BASE)}
    rows(Path(args.saida)/"M1.2.1-arquivos-react-navegador.csv",data,["pacote","arquivo","classe","exemplo_alcancado"])
    jout(Path(args.saida)/"M1.2.1-resumo.json",resumo)
    print("Dependências diretas e transitivas de React/navegador consolidadas.")


def cloc(args):
    inv=jread(args.inventario); valid=set(inv["producao"])
    raw=jread(args.cloc)
    csvrows=[]; sem=[]
    for f in sorted(valid):
        found=raw.get(f) or raw.get("./"+f)
        if not isinstance(found,dict):
            sem.append(f); continue
        n=found.get("code")
        if n is None: raise SystemExit("cloc sem campo code para: "+f)
        csvrows.append({"arquivo":f,"pacote":pacote(f),"loc":n,"extenso":int(n>1000)})
    if sem: raise SystemExit(f"cloc não contou {len(sem)} arquivos; amostra: {sem[:3]}. Verifique inclusão de TSX/TS.")
    out=Path(args.saida)
    rows(out/"M1.4.2-linhas-arquivos.csv",csvrows,["arquivo","pacote","loc","extenso"])
    grandes=[r for r in csvrows if r["extenso"]]
    jout(out/"M1.4.2-resumo.json",{"total_arquivos":len(csvrows),"extensos":len(grandes),"percentual":100*len(grandes)/len(csvrows) if csvrows else None,"arquivos_extensos":[r["arquivo"] for r in grandes]})
    print(f"LOC: {len(grandes)} de {len(csvrows)} arquivos > 1000 LOC.")


def cobertura(args):
    raw=jread(args.cobertura); inv=jread(args.inventario)
    files={norm(p):d for p,d in raw.items() if p!="total"}
    acc=defaultdict(lambda:[0,0]); missing=[]
    for p in inv["producao"]:
        records=[d for name,d in files.items() if name.endswith(p)]
        if len(records)!=1:
            missing.append(p); continue
        lines=records[0].get("lines",{})
        for key in ("total","covered"):
            if key not in lines: raise SystemExit(f"Resumo de cobertura sem lines.{key}: {p}")
        acc[pacote(p)][0]+=lines["covered"];acc[pacote(p)][1]+=lines["total"]
    out=Path(args.saida)
    rows(out/"M1.5.1-cobertura-pacotes.csv",[{"pacote":p,"linhas_executadas":c,"linhas_executaveis":t,"percentual":round(100*c/t,4) if t else "N/A"} for p,(c,t) in sorted(acc.items())],["pacote","linhas_executadas","linhas_executaveis","percentual"])
    jout(out/"M1.5.1-arquivos-nao-reportados.json",{"total":len(missing),"arquivos":missing})
    print(f"Cobertura tabulada; {len(missing)} arquivos do inventário sem entrada no relatório. Conferir include/exclude do Vitest e NÃO presumir cobertura nula automaticamente.")


def testes(args):
    inv=jread(args.inventario); root=Path(args.src)
    data=[]
    for p in inv["testes"]:
        s=(root/p).read_text(encoding="utf-8",errors="replace")
        if re.search(r"from\s*['\"](?:@playwright/test|playwright|puppeteer|cypress)|\b(cy\.|page\.goto\(|test\.describe\()",s):
            sug="ponta_a_ponta"
        elif re.search(r"\brender\s*\(|\btest-utils\b",s): sug="integracao"
        else: sug="unitario"
        data.append({"arquivo":p,"sugestao":sug,"classe_confirmada":"", "evidencia":"", "revisor":""})
    rows(args.out,data,["arquivo","sugestao","classe_confirmada","evidencia","revisor"])
    print(f"Planilha com {len(data)} suítes gerada. Preencher classe_confirmada após inspeção, antes do cálculo.")


def testes_resumo(args):
    with open(args.planilha,encoding="utf-8",newline="") as f: data=list(csv.DictReader(f))
    vals=[x["classe_confirmada"].strip() for x in data]
    good={"unitario","integracao","ponta_a_ponta"}
    if not data or any(x not in good for x in vals):raise SystemExit("Todas as linhas precisam de classe_confirmada: unitario, integracao ou ponta_a_ponta")
    total=len(data); out={x:{"arquivos":vals.count(x),"percentual":round(100*vals.count(x)/total,4)} for x in sorted(good)}
    jout(args.out,{"total_suites":total,"classes":out})
    print(f"M1.5.2: {total} suítes auditadas.")


def historico(args):
    prs=jread(args.prs)
    if not isinstance(prs,list):raise SystemExit("prs.json deve ser lista de PRs, com number, merged_at, author, files e CI")
    extended=set(jread(args.extensos)["arquivos_extensos"])
    rows_pr=[]; ci=[]; falta=[]
    for p in prs:
        if p.get("excluir") not in (True,False): raise SystemExit(f"PR {p.get('number')}: classifique excluir=true/false (bots, traduções, dependências)")
        if p["excluir"]:continue
        if not isinstance(p.get("files"),list):raise SystemExit("PR sem lista de arquivos: "+str(p.get("number")))
        files=p["files"]
        prod_files={f.get("filename") for f in files if prod(str(f.get("filename","")))}
        # Renomes: contar origem/destino relevantes para histórico, preservando ambos.
        changed_extenso=bool(extended & (prod_files | {f.get("previous_filename") for f in files if f.get("previous_filename")}))
        rows_pr.append({"pr":p["number"],"alterados_producao":len(prod_files),"alterou_extenso":int(changed_extenso)})
        if p.get("ci_status") in ("executado","nao_executado","sem_evidencia"):
            ci.append({"pr":p["number"],"ci_status":p["ci_status"]})
        else: falta.append(p["number"])
    if falta:raise SystemExit("PRs sem status CI validado (executado, nao_executado, sem_evidencia): "+str(falta[:8]))
    nums=[r["alterados_producao"] for r in rows_pr]
    out=Path(args.saida); rows(out/"M1.4.1-M1.4.3-prs.csv",rows_pr,["pr","alterados_producao","alterou_extenso"])
    rows(out/"M1.5.3-ci-prs.csv",ci,["pr","ci_status"])
    denom=sum(x["ci_status"]!="sem_evidencia" for x in ci)
    success=sum(x["ci_status"]=="executado" for x in ci)
    jout(out/"M1.4.1-M1.4.3-M1.5.3-resumo.json",{
        "prs_incluidos":len(rows_pr),
        "M1.4.1_mediana_arquivos":statistics.median(nums) if nums else None,
        "M1.4.3_percentual_prs_em_extensos":round(100*sum(x["alterou_extenso"] for x in rows_pr)/len(rows_pr),4) if rows_pr else None,
        "M1.5.3_percentual_execucao_testes":round(100*success/denom,4) if denom else None,
        "M1.5.3_n_com_evidencia":denom,"M1.5.3_n_sem_evidencia":len(ci)-denom,
    })
    print(f"Histórico processado: {len(rows_pr)} PRs, CI suficiente em {denom}. Verifique a classificação humana/exclusões.")


def main():
    p=argparse.ArgumentParser(description=__doc__)
    sub=p.add_subparsers(dest="comando",required=True)
    def cmd(n,func,**opts):
        x=sub.add_parser(n)
        for name,kw in opts.items():x.add_argument("--"+name.replace("_","-"),required=True,help=kw)
        x.set_defaults(func=func)
    cmd("inventario",inventario,src="Diretório do Excalidraw",out="Saída do inventário JSON")
    cmd("grafo",grafo,inventario="Inventário JSON",grafo="Madge grafo JSON",saida="Diretório de consolidados")
    cmd("navegador",navegador,inventario="Inventário JSON",grafo="Grafo Madge JSON",diretos="JSON com lista de arquivos de dependência direta auditada",saida="Diretório de consolidados")
    cmd("cloc",cloc,inventario="Inventário JSON",cloc="JSON do cloc --by-file",saida="Diretório de consolidados")
    cmd("cobertura",cobertura,inventario="Inventário JSON",cobertura="coverage-summary.json do Vitest",saida="Diretório de consolidados")
    cmd("testes",testes,inventario="Inventário JSON",src="Diretório Excalidraw",out="Planilha CSV de auditoria")
    cmd("testes-resumo",testes_resumo,planilha="CSV auditado com classe_confirmada",out="Arquivo JSON")
    cmd("historico",historico,prs="JSON de PRs revisado",extensos="Resumo JSON de M1.4.2",saida="Diretório de consolidados")
    args=p.parse_args();args.func(args)

if __name__=="__main__":main()
