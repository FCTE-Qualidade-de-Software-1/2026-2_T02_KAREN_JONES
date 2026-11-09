import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT=Path(__file__).parents[1]/'scripts/g1_preparar_prs.py'

class TestPrepararPR(unittest.TestCase):
    def test_execucao_antes_do_merge(self):
        with tempfile.TemporaryDirectory() as dirname:
            root=Path(dirname);prs=root/'prs';prs.mkdir()
            (prs/'numeros.txt').write_text('123\n')
            (prs/'pr-123.json').write_text(json.dumps({'number':123,'title':'fix: teste','user':{'login':'dev'},'merged_at':'2026-10-15T10:00:00Z','head':{'sha':'abc123'},'base':{'ref':'master'}}))
            (prs/'pr-123-files.json').write_text(json.dumps([[{'filename':'packages/common/src/a.ts','status':'modified'}]]))
            (prs/'pr-123-runs.json').write_text(json.dumps([{'workflow_runs':[{'id':42,'head_sha':'abc123','event':'pull_request'}]}]))
            (prs/'pr-123-run-42-jobs.json').write_text(json.dumps([{'jobs': [{'id': 51, 'steps': [{'name': 'Test Coverage', 'conclusion': 'success', 'completed_at': '2026-10-15T09:59:00Z'}]}]}]))
            outfile=root/'audit.json'
            p=subprocess.run([sys.executable,str(SCRIPT),'--pasta-brutos',str(root),'--out',str(outfile)],capture_output=True,text=True)
            self.assertEqual(p.returncode,0,p.stderr)
            row=json.loads(outfile.read_text())[0]
            self.assertEqual(row['ci_status'],'executado')
            self.assertIsNone(row['excluir'])
            self.assertEqual(len(row['evidencia_ci']),1)

if __name__=='__main__':unittest.main()
