import csv
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SOURCE=Path(__file__).parents[1] / 'scripts/g1_processar.py'
spec=importlib.util.spec_from_file_location('g1',SOURCE)
g1=importlib.util.module_from_spec(spec);spec.loader.exec_module(g1)

class TestG1(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.root=Path(self.tmp.name)
    def tearDown(self):self.tmp.cleanup()
    def write(self,n,obj):
        p=self.root/n;p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(json.dumps(obj),encoding='utf-8');return str(p)
    def args(self,**kwargs):return type('Args',(),kwargs)()

    def test_grafo_pares_e_instabilidade(self):
        inv=self.write('inventario.json',{'producao':['packages/common/src/a.ts','packages/utils/src/b.ts','packages/math/src/c.ts','packages/excalidraw/index.tsx','excalidraw-app/a.tsx'],'pacotes':['common','utils','math','excalidraw','excalidraw-app']})
        graph=self.write('grafo.json',{
            'packages/common/src/a.ts':['packages/utils/src/b.ts','packages/excalidraw/index.tsx'],
            'packages/utils/src/b.ts':['packages/common/src/a.ts'],
            'packages/math/src/c.ts':[],
            'packages/excalidraw/index.tsx':['excalidraw-app/a.tsx'],
            'excalidraw-app/a.tsx':[]})
        g1.grafo(self.args(inventario=inv,grafo=graph,saida=self.root/'c'))
        cycles=json.loads((self.root/'c/M1.1.1-pares-ciclicos.json').read_text())
        self.assertEqual(cycles['total_pares'],1)
        with (self.root/'c/M1.1.2-violacoes.csv').open() as f:
            r=list(csv.DictReader(f))
        self.assertEqual(len(r),2)
        with (self.root/'c/M1.1.3-acoplamento.csv').open() as f:
            vals=list(csv.DictReader(f))
        self.assertEqual([p for p in vals if p['pacote']=='math'][0]['I'],'')

    def test_cloc_estrito_mais_de_mil(self):
        inv=self.write('inv.json',{'producao':['packages/common/src/a.ts','packages/common/src/b.tsx']})
        cl=self.write('cloc.json',{'header':{},'packages/common/src/a.ts':{'code':1000,'comment':0,'blank':0},'packages/common/src/b.tsx':{'code':1001,'comment':0,'blank':0}})
        g1.cloc(self.args(inventario=inv,cloc=cl,saida=self.root/'c'))
        r=json.loads((self.root/'c/M1.4.2-resumo.json').read_text())
        self.assertEqual(r['extensos'],1)
        self.assertEqual(r['percentual'],50.0)

    def test_navegador_alcance_transitivo(self):
        inv=self.write('inv.json',{'producao':['packages/common/src/a.ts','packages/utils/src/b.ts','packages/math/src/c.ts']})
        graph=self.write('graph.json',{'packages/common/src/a.ts':['packages/utils/src/b.ts'],'packages/utils/src/b.ts':['packages/math/src/c.ts'],'packages/math/src/c.ts':[]})
        direct=self.write('direct.json',{'diretos':['packages/math/src/c.ts']})
        g1.navegador(self.args(inventario=inv,grafo=graph,diretos=direct,saida=self.root/'c'))
        r=json.loads((self.root/'c/M1.2.1-resumo.json').read_text())
        self.assertEqual(r['math']['diretas'],1)
        self.assertEqual(r['utils']['transitivas_apenas'],1)
        self.assertEqual(r['common']['transitivas_apenas'],1)

    def test_historico_e_ci_com_ausencia_excluida(self):
        prs=self.write('prs.json',[
            {'number':1,'excluir':False,'files':[{'filename':'packages/math/src/a.ts'}],'ci_status':'executado'},
            {'number':2,'excluir':False,'files':[{'filename':'README.md'}],'ci_status':'nao_executado'},
            {'number':3,'excluir':False,'files':[{'filename':'packages/math/src/b.ts'}],'ci_status':'sem_evidencia'},
            {'number':4,'excluir':True,'files':[{'filename':'packages/math/src/b.ts'}],'ci_status':'executado'},
        ])
        large=self.write('grandes.json',{'arquivos_extensos':['packages/math/src/b.ts']})
        g1.historico(self.args(prs=prs,extensos=large,saida=self.root/'c'))
        r=json.loads((self.root/'c/M1.4.1-M1.4.3-M1.5.3-resumo.json').read_text())
        self.assertEqual(r['M1.4.1_mediana_arquivos'],1)
        self.assertAlmostEqual(r['M1.4.3_percentual_prs_em_extensos'],100/3,places=4)
        self.assertEqual(r['M1.5.3_percentual_execucao_testes'],50)
        self.assertEqual(r['M1.5.3_n_sem_evidencia'],1)

if __name__=='__main__':unittest.main()
