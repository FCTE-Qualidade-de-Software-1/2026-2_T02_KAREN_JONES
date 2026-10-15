
# Interessados no projeto Excalidraw

## 1. Usuários finais

Utilizam o Excalidraw para criar e editar desenhos, diagramas e esboços, individualmente ou em colaboração. Podem acessar a aplicação por computadores ou dispositivos móveis, com mouse, teclado, toque ou caneta.

**Principais interesses:**

- Estabilidade e comportamento consistente do editor.
- Preservação dos desenhos e recuperação do trabalho após interrupções.
- Continuidade da edição diante de falhas de rede ou colaboração.
- Funcionamento offline e uso em diferentes navegadores.
- Uso adequado em dispositivos móveis, inclusive com toque e caneta.
- Exportação dos desenhos para outras ferramentas.

**Aspectos da avaliação associados:**

- **Disponibilidade:** funcionamento das funções essenciais sem conexão, após o primeiro carregamento; possibilidade de usar o editor local sem sessão colaborativa; dependência de recursos e serviços externos.
- **Tolerância a falhas:** isolamento entre edição local e colaboração, tratamento de exceções, arquivos inválidos ou corrompidos, limites de armazenamento do navegador e mensagens que orientem o usuário.
- **Recuperabilidade:** armazenamento e salvamento local, persistência e reabertura dos desenhos, restauração automática do último estado, arquivos de versões anteriores, desfazer/refazer e reconciliação após reconexão.
- **Adaptabilidade:** navegadores e versões suportados, diferentes sistemas operacionais via navegador, tamanhos de tela, toque, caneta e alternativas para APIs web indisponíveis, como canvas, área de transferência e acesso a arquivos.
- **Substituibilidade:** acesso aos dados fora do editor, documentação de formatos, exportação em `.excalidraw`, PNG e SVG, reimportação sem perda relevante e migração entre ferramentas, quando disponível.

Na matriz de prioridades, a **confiabilidade é principal**, a **portabilidade é secundária** e a **manutenibilidade é indireta ou não aplicável**. Na rastreabilidade, usuários finais são interessados principais em disponibilidade, tolerância a falhas, recuperabilidade, adaptabilidade e substituibilidade. Os artefatos relacionados são configurações de PWA/offline, código de colaboração e erros, persistência, importação/exportação, compatibilidade e dependências.

## 2. Desenvolvedores do projeto

Compreendem, modificam e ampliam o código do Excalidraw. Trabalham com TypeScript e React em um monorepo que separa aplicação, biblioteca e pacotes especializados.

**Principais interesses:**

- Organização e compreensão claras do código.
- Baixo acoplamento e separação de responsabilidades entre módulos.
- Facilidade para adicionar funcionalidades e corrigir defeitos.
- Capacidade de testar mudanças sem provocar efeitos indesejados.
- Documentação da arquitetura e das convenções de código.
- Análise estática, tipagem, lint e formatação padronizada.

**Aspectos da avaliação associados:**

- **Modularidade:** limites entre `excalidraw-app/` e `packages/excalidraw/`, coesão dos pacotes, direção das dependências, ausência de ciclos e isolamento das funcionalidades.
- **Analisabilidade:** estrutura de diretórios, clareza das responsabilidades, nomes e comentários, documentação, guias de arquitetura/contribuição, TypeScript, análise estática, mensagens de erro e logs.
- **Modificabilidade:** impacto entre componentes, concentração excessiva de responsabilidades, acoplamento do estado global à interface, atualização de dependências e alcance das alterações no histórico de commits e *pull requests*.
- **Testabilidade:** testes isolados e automatizados, organização dos cenários e integração ao desenvolvimento.

Na matriz, a **manutenibilidade é principal**, a **confiabilidade é secundária** e a **portabilidade é indireta ou não aplicável**. A rastreabilidade os vincula principalmente a modularidade, analisabilidade e modificabilidade. As evidências previstas incluem pacotes, aplicação, dependências, diretórios, configurações de TypeScript/lint, documentação e histórico de alterações.

## 3. Mantenedores

Respondem pela continuidade e evolução do projeto. Seu foco abrange a estabilidade das versões, o controle de mudanças, a qualidade das contribuições e a manutenção da base técnica.

**Principais interesses:**

- Prevenir regressões e controlar a complexidade do software.
- Facilitar a manutenção e preservar a qualidade ao longo do tempo.
- Manter a estabilidade do desenvolvimento e a compatibilidade entre versões.
- Revisar e integrar contribuições com verificações automáticas.
- Gerenciar dependências externas e suas atualizações.
- Organizar versões e publicação do pacote.

**Aspectos da avaliação associados:**

- **Modularidade e modificabilidade:** estrutura do código, dependências e efeitos das alterações.
- **Testabilidade:** testes automatizados, configurações de teste e fluxos de integração contínua.
- **Maturidade:** revisão de código, controle de alterações, verificação automática de tipos/lint/testes, identificação, registro, classificação e resolução de defeitos, prevenção de regressões e estabilidade/regularidade das versões publicadas.

Na matriz, **manutenibilidade e confiabilidade são principais** e **portabilidade é secundária**. Na rastreabilidade, os mantenedores são principais em modularidade, modificabilidade, testabilidade e maturidade. As fontes de evidência incluem código e dependências, commits, *pull requests*, testes, `.github/workflows/` e histórico de *issues*.

## 4. Contribuidores open source

São participantes externos que podem colaborar com o desenvolvimento do Excalidraw. Precisam compreender o projeto e validar suas alterações antes de submetê-las.

**Principais interesses:**

- Entender a estrutura do repositório e localizar os componentes a alterar.
- Configurar o ambiente de desenvolvimento.
- Executar testes e verificar se as mudanças causam problemas.
- Encontrar orientações claras para contribuir e enviar alterações.
- Receber retorno rápido das verificações automáticas.

**Aspectos da avaliação associados:**

- **Analisabilidade:** diretórios, documentação, convenções, guias de contribuição, tipagem, lint e formatação.
- **Instalabilidade:** pré-requisitos, versões das ferramentas, dependências, arquivo de lock, instruções e etapas manuais para executar o projeto.
- **Testabilidade e modificabilidade:** reprodução de cenários, testes automatizados e impacto das mudanças propostas.

Na matriz, a **manutenibilidade é principal**; **confiabilidade e portabilidade são secundárias**. A rastreabilidade os identifica como principais em analisabilidade e instalabilidade. Os artefatos associados são diretórios, TypeScript/lint, documentação, `package.json`, `Dockerfile` e instruções de instalação.

## 5. Desenvolvedores que integram a biblioteca

Incorporam o pacote `@excalidraw/excalidraw` a outras aplicações React. Dependem de uma interface pública estável e de integração viável em ambientes distintos.

**Principais interesses:**

- Instalação simples e documentação adequada.
- Estabilidade e tipagem clara da interface pública.
- Compatibilidade com diferentes versões de React.
- Facilidade de integração e atualização da biblioteca.
- Política de versionamento e registro de mudanças incompatíveis.
- Funcionamento com diferentes empacotadores e ambientes de renderização.

**Aspectos da avaliação associados:**

- **Reusabilidade:** separação da biblioteca e aplicação oficial, componentes reutilizáveis, API pública, propriedades e callbacks, documentação, exemplos e possível reutilização de pacotes menores.
- **Adaptabilidade:** versões de React, dependências, APIs web exigidas, empacotadores e aplicações com renderização no servidor (SSR).
- **Instalabilidade:** gerenciadores de pacotes, pré-requisitos, dependências obrigatórias e facilidade de atualizar/remover a biblioteca.
- **Substituibilidade:** formatos de dados, importação/exportação e integração com outras ferramentas.

Na matriz, a **portabilidade é principal**; **manutenibilidade e confiabilidade são secundárias**. A rastreabilidade os identifica como principais em reusabilidade, adaptabilidade, instalabilidade e substituibilidade. As evidências incluem `packages/excalidraw/`, `examples/`, API pública, configurações de compatibilidade, dependências, `package.json` e recursos de importação/exportação.

## 6. Equipes de implantação e operação

São responsáveis por construir, configurar, implantar ou hospedar a aplicação em ambientes próprios, inclusive com Docker.

**Principais interesses:**

- Construção e implantação simples e previsíveis.
- Compatibilidade com diferentes ambientes.
- Possibilidade de uso de Docker.
- Facilidade de configurar a aplicação.
- Documentação dos pré-requisitos e etapas de build e execução.
- Reprodutibilidade do build em ambientes distintos.

**Aspectos da avaliação associados:**

- **Instalabilidade:** ferramentas e versões exigidas, dependências, configurações, etapas de construção, Docker, instruções de execução e reprodução do build.
- **Disponibilidade:** funcionamento da aplicação em diferentes condições, suporte offline e dependência de recursos externos.

Na matriz, a **portabilidade é principal**, a **confiabilidade é secundária** e a **manutenibilidade é indireta ou não aplicável**. A rastreabilidade as vincula principalmente à disponibilidade e instalabilidade. Os artefatos associados incluem configuração de PWA/offline em `excalidraw-app/`, `package.json`, `Dockerfile` e documentação de instalação.

## 7. Equipes de qualidade

Atuam na validação contínua do comportamento do software. Precisam detectar regressões, reproduzir defeitos e confirmar as consequências das mudanças.

**Principais interesses:**

- Existência e organização de testes.
- Detecção de regressões e reprodução de defeitos.
- Organização do código e validação das alterações.
- Rastreabilidade entre defeitos relatados, correções e testes.
- Integração dos testes à integração contínua.

**Aspectos da avaliação associados:**

- **Testabilidade:** testes automatizados e isolados, níveis unitário, integração e, quando existente, ponta a ponta; simulação de mouse, teclado e toque no editor baseado em canvas; reprodução de cenários e execução automática na integração contínua. A cobertura será tratada como evidência na Fase 02.
- **Maturidade:** revisão de código, verificação de tipos, lint, testes, gestão de defeitos, controle de alterações e prevenção de regressões.

Na matriz, **manutenibilidade e confiabilidade são principais** e **portabilidade é secundária**. A rastreabilidade as relaciona principalmente a testabilidade e maturidade. Os artefatos previstos são testes, configurações, `.github/workflows/`, integração contínua e histórico de *issues*.

## 8. Equipe avaliadora e docentes

A equipe avaliadora conduz a análise acadêmica; os docentes acompanham seus resultados. O trabalho avalia a **qualidade do produto**, de forma independente, com artefatos públicos, tempo e recursos limitados e sem acesso à infraestrutura de produção.

**Principais interesses:**

- Requisitos claros, específicos e rastreáveis.
- Alinhamento à família de normas SQuaRE.
- Escopo realista e explicitamente delimitado.
- Evidências e procedimentos verificáveis e reproduzíveis.
- Registro do commit ou tag e da data da versão analisada.
- Ligação de cada requisito a uma característica, subcaracterística e pelo menos um interessado.

**Referências e limites associados:**

- A ISO/IEC 25010 orienta o modelo de qualidade; a ISO/IEC 25040, o processo; a ISO/IEC 25030, os requisitos; e as ISO/IEC 25020 e 25023, as medidas futuras da Fase 02.
- O documento adota subcaracterísticas da ISO/IEC 25010:2011 e aponta a necessidade de confirmar com o professor a edição a utilizar, diante de renomeações em 2023.
- A Fase 01 identifica requisitos: não define métricas, fórmulas, critérios, pesos ou ferramentas, nem executa testes ou apresenta resultados e julgamentos. Esses itens pertencem às fases posteriores.

**Não há classificação formal de prioridades** para equipe avaliadora e docentes na matriz da seção 4.10, nem associação específica na tabela de rastreabilidade da seção 10.5.

## 9. Comunidade e organizações que adotam o produto

Adotam o Excalidraw em atividades de **documentação, ensino e reuniões**. Seu interesse está na continuidade do uso e no acesso aos conteúdos produzidos.

**Principais interesses:**

- Continuidade do projeto.
- Estabilidade entre versões.
- Possibilidade de transferir dados para outras ferramentas, quando necessário.

Essas necessidades se relacionam à confiabilidade, à compatibilidade entre versões e à portabilidade de dados. O documento menciona exportação em `.excalidraw`, PNG e SVG. **Essa associação é descritiva:** a matriz da seção 4.10 e a tabela da seção 10.5 não atribuem prioridades ou subcaracterísticas específicas a esse grupo.

## Matriz de prioridades dos interessados

A seção 4.10 apresenta as prioridades dos sete grupos abaixo. **Principal**, **secundário** e **indireto/não aplicável** reproduzem, respectivamente, os símbolos ●, ○ e – do documento.

| Interessado | Manutenibilidade | Confiabilidade | Portabilidade |
|---|---|---|---|
| Usuários finais | Indireto/não aplicável | Principal | Secundário |
| Desenvolvedores do projeto | Principal | Secundário | Indireto/não aplicável |
| Mantenedores | Principal | Principal | Secundário |
| Contribuidores open source | Principal | Secundário | Secundário |
| Desenvolvedores que integram a biblioteca | Secundário | Secundário | Principal |
| Equipes de implantação e operação | Indireto/não aplicável | Secundário | Principal |
| Equipes de qualidade | Principal | Principal | Secundário |

A equipe avaliadora/docentes e a comunidade/organizações adotantes também são interessadas, mas **não constam da matriz**.

## Rastreabilidade entre interessados e subcaracterísticas

A tabela da seção 10.5 identifica **interessados principais por subcaracterística** e os artefatos previstos como evidência. Essas relações não alteram a matriz de prioridades acima.

| Subcaracterística | Interessados principais | Artefatos relacionados |
|---|---|---|
| Modularidade | Desenvolvedores; mantenedores | `packages/`, `excalidraw-app/`, arquivos de dependências |
| Reusabilidade | Integradores da biblioteca | `packages/excalidraw/`, `examples/`, interface pública |
| Analisabilidade | Contribuidores; desenvolvedores | Diretórios, configurações de TypeScript e lint, documentação |
| Modificabilidade | Desenvolvedores; mantenedores | Código dos pacotes, commits, *pull requests* |
| Testabilidade | Equipes de qualidade; mantenedores | Arquivos/configurações de teste, `.github/workflows/` |
| Maturidade | Mantenedores; equipes de qualidade | Integração contínua, testes, histórico de *issues* |
| Disponibilidade | Usuários finais; operação | Configuração de PWA e offline em `excalidraw-app/` |
| Tolerância a falhas | Usuários finais | Código de colaboração e tratamento de erros |
| Recuperabilidade | Usuários finais | Persistência local, importação/exportação `.excalidraw` |
| Adaptabilidade | Usuários finais; integradores | Compatibilidade e dependências declaradas |
| Instalabilidade | Integradores; operação; contribuidores | `package.json`, `Dockerfile`, documentação de instalação |
| Substituibilidade | Usuários finais; integradores | Funcionalidades de importação/exportação |

## Histórico de Versões
| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| ------ | ---- | --------- | --------- | ----------- |
| 0.1 | 04/10/2026 | Documento dos possíveis interessados nesse projeto | [Davi Pierre](https://gitlab.com/DaviPierre) | |



