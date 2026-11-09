#!/usr/bin/env node
"use strict";
/**
 * Extrator AST para G1 — usa TypeScript do checkout fixado do Excalidraw.
 * Leitura apenas; nenhum arquivo do produto é alterado.
 *
 * node scripts/g1_typescript.cjs mapear --src /caminho/excalidraw --inventario ... --saida ...
 * node scripts/g1_typescript.cjs complexidade --src /caminho/excalidraw --inventario ... --eslint ... --saida ...
 */
const fs = require("node:fs");
const path = require("node:path");
const { createRequire } = require("node:module");

function args() {
  const result = { command: process.argv[2] };
  for (let i = 3; i < process.argv.length; i += 2) {
    const key = process.argv[i];
    if (!key.startsWith("--") || !process.argv[i+1]) throw new Error("Argumento ausente: " + key);
    result[key.slice(2)] = process.argv[i + 1];
  }
  if (!["mapear", "complexidade"].includes(result.command)) throw new Error("Escolha mapear ou complexidade");
  for (const key of ["src", "inventario", "saida"]) if (!result[key]) throw new Error("Falta --" + key);
  if (result.command === "complexidade" && !result.eslint) throw new Error("Falta --eslint");
  return result;
}
function json(file) { return JSON.parse(fs.readFileSync(file,"utf8")); }
function writeJSON(file, data) {fs.mkdirSync(path.dirname(file),{recursive:true});fs.writeFileSync(file,JSON.stringify(data,null,2)+"\n");}
function csvValue(val) {const s=String(val??"");return /[",\n]/.test(s)?`"${s.replaceAll('"','""')}"`:s;}
function csv(file, columns, records) {
  fs.mkdirSync(path.dirname(file),{recursive:true});
  fs.writeFileSync(file, [columns.join(","),...records.map(r=>columns.map(c=>csvValue(r[c])).join(","))].join("\n")+"\n");
}
function sourceFile(ts,filename) {
  const code=fs.readFileSync(filename,"utf8");
  return ts.createSourceFile(filename,code,ts.ScriptTarget.Latest,true,filename.endsWith(".tsx")?ts.ScriptKind.TSX:ts.ScriptKind.TS);
}
function walk(ts, node, fn) {fn(node);ts.forEachChild(node,c=>walk(ts,c,fn));}
function linha(sf,pos) {return sf.getLineAndCharacterOfPosition(pos).line+1;}
function isFunction(ts,node) {return ts.isFunctionDeclaration(node) || ts.isFunctionExpression(node) || ts.isArrowFunction(node) || ts.isMethodDeclaration(node) || ts.isConstructorDeclaration(node) || ts.isGetAccessorDeclaration(node) || ts.isSetAccessorDeclaration(node);}
function linhaCodigo(ts,sf,node,allFns) {
  const start=node.getStart(sf),end=node.end;
  const occupied=new Set();
  const scanner=ts.createScanner(ts.ScriptTarget.Latest,true,sf.languageVariant,sf.text);
  while(scanner.scan()!==ts.SyntaxKind.EndOfFileToken){
    const a=scanner.getTokenPos(), b=scanner.getTextPos();
    if(a<start||a>=end) continue;
    const l1=linha(sf,a),l2=linha(sf,Math.max(a,b-1));
    for(let l=l1;l<=l2;l++)occupied.add(l);
  }
  for(const inner of allFns){
    if(inner===node)continue;
    const a=inner.getStart(sf),b=inner.end;
    if(start<=a && b<=end){
      for(let l=linha(sf,a);l<=linha(sf,b-1);l++)occupied.delete(l);
    }
  }
  return occupied.size;
}
function main(){
  const a=args(),src=path.resolve(a.src), out=path.resolve(a.saida);
  const ts=createRequire(path.join(src,"package.json"))("typescript");
  const inv=json(a.inventario);
  if(a.command==="mapear"){
    const direct=[], props=[];
    for(const f of inv.producao){
      const sf=sourceFile(ts,path.join(src,f));
      walk(ts,sf,node=>{
        if(ts.isImportDeclaration(node)&&node.moduleSpecifier&&ts.isStringLiteral(node.moduleSpecifier)){
          const value=node.moduleSpecifier.text;
          const clause=node.importClause;
          const onlyType=clause?.isTypeOnly || (clause && !clause.name && clause.namedBindings && ts.isNamedImports(clause.namedBindings) && clause.namedBindings.elements.length>0 && clause.namedBindings.elements.every(el=>el.isTypeOnly));
          if(!onlyType && /^(react|react-dom)(\/|$)/.test(value)){
            direct.push({arquivo:f,linha:linha(sf,node.getStart(sf)),evidencia:`import ${value}`,validado:""});
          }
        }
        // Não conta menções em strings ou comentários; casos de variáveis locais devem ser auditados.
        if(ts.isPropertyAccessExpression(node) && ts.isIdentifier(node.expression) && ["window","document"].includes(node.expression.text)){
          direct.push({arquivo:f,linha:linha(sf,node.getStart(sf)),evidencia:node.expression.text+"."+node.name.text,validado:""});
        }
        if(f==="packages/excalidraw/types.ts" && ts.isInterfaceDeclaration(node) && node.name.text==="ExcalidrawProps"){
          for(const member of node.members){
            const prop=member.name?.getText(sf).replace(/^['"]|['"]$/g,"");
            if(prop)props.push({propriedade:prop,linha:linha(sf,member.getStart(sf)),documentada:"",caminho_documentacao:"",trecho_evidencia:""});
          }
        }
      });
    }
    csv(path.join(out,"M1.2.1-sementes-para-auditoria.csv"),["arquivo","linha","evidencia","validado"],direct);
    csv(path.join(out,"M1.2.2-propriedades-para-auditoria.csv"),["propriedade","linha","documentada","caminho_documentacao","trecho_evidencia"],props);
    writeJSON(path.join(out,"M1.2.1-diretos-candidatos.json"),{"diretos":[...new Set(direct.map(r=>r.arquivo))].sort()});
    console.log(`Candidatos diretos: ${direct.length} ocorrências; ${props.length} propriedades públicas. Audite os CSVs antes do cálculo.`);
    if(!props.length)process.exitCode=2;
    return;
  }
  const eslint=json(a.eslint), sourceNames=new Set(inv.producao);
  const rows=[],anomalies=[];
  for(const file of eslint){
    const relative=path.relative(src,path.resolve(file.filePath)).replaceAll("\\","/");
    if(!sourceNames.has(relative))continue;
    const sf=sourceFile(ts,path.join(src,relative));
    const fns=[];walk(ts,sf,node=>{if(isFunction(ts,node))fns.push(node);});
    const warnings=(file.messages||[]).filter(m=>m.ruleId==="complexity");
    if(file.fatalErrorCount>0)anomalies.push({arquivo:relative,erro:"fatal-error-eslint"});
    const used=new Set();
    for(const w of warnings){
      const m=/complexity of (\d+)/i.exec(w.message);
      if(!m){anomalies.push({arquivo:relative,linha:w.line,erro:"mensagem-complexidade-nao-interpretada",texto:w.message});continue;}
      const at=w.line;
      const compatible=fns.map((n,i)=>({n,i,start:linha(sf,n.getStart(sf)),end:linha(sf,n.end-1)})).filter(x=>x.start<=at&&at<=x.end&&!used.has(x.i));
      // Preferir a menor função aninhada que abrange a posição do diagnóstico.
      compatible.sort((a,b)=>(a.end-a.start)-(b.end-b.start));
      if(!compatible.length){anomalies.push({arquivo:relative,linha:at,erro:"funcao-nao-correspondida",texto:w.message});continue;}
      const v=compatible[0];used.add(v.i);
      const loc=linhaCodigo(ts,sf,v.n,fns);
      const cc=Number(m[1]);const faixa=cc<=10?"baixo":cc<=20?"moderado":cc<=50?"alto":"muito_alto";
      rows.push({arquivo:relative,linha:at,complexidade:cc,loc_proprias:loc,faixa});
    }
    const missing=fns.length-used.size;
    if(missing)anomalies.push({arquivo:relative,erro:"funcoes-sem-diagnostico",quantidade:missing});
  }
  csv(path.join(out,"M1.3.1-funcoes-complexidade.csv"),["arquivo","linha","complexidade","loc_proprias","faixa"],rows);
  writeJSON(path.join(out,"M1.3.1-anomalias-para-auditoria.json"),anomalies);
  const totals={};for(const r of rows){const o=totals[r.faixa]||(totals[r.faixa]={funcoes:0,linhas:0});o.funcoes++;o.linhas+=r.loc_proprias;}
  const total=rows.reduce((s,r)=>s+r.loc_proprias,0);
  writeJSON(path.join(out,"M1.3.1-resumo.json"),{totais:totals,total_linhas_proprias:total,percentuais:Object.fromEntries(Object.entries(totals).map(([k,v])=>[k,total?100*v.linhas/total:null])),anomalias:anomalies.length});
  console.log(`Complexidade: ${rows.length} diagnósticos cruzados; ${anomalies.length} anomalias. Auditoria obrigatória antes da pontuação.`);
  if(anomalies.length)process.exitCode=2;
}
try{main()}catch(e){console.error(e.stack||e);process.exit(1);}
