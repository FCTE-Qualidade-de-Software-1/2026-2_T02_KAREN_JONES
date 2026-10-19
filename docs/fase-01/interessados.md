
# Interessados no projeto Excalidraw

Identificar as partes interessadas é uma etapa obrigatória do processo de avaliação definido pela ISO/IEC 25040. Mais do que preencher um campo do documento, o mapeamento dos interessados é o que nos ajuda a escolher *o que* avaliar e a entender *por que* determinadas características importam mais do que outras.

O Excalidraw tem um perfil de usuários bastante diversificado. Não estamos falando de um sistema interno com um público bem definido — é uma ferramenta web open source usada por desenvolvedores, designers, professores, estudantes e equipes de engenharia em contextos completamente diferentes. Isso torna o mapeamento de interessados especialmente relevante.

## 1. Usuários finais

São as pessoas que abrem o Excalidraw no navegador para criar diagramas, esboços e apresentações. Podem estar sozinhos ou colaborando em tempo real com outras pessoas. Usam mouse, teclado, toque na tela ou caneta dependendo do dispositivo.

Para esse grupo, o que importa é simples: a ferramenta precisa funcionar. Os desenhos precisam ser salvos. Se a conexão cair, o trabalho não pode ser perdido. Se outra pessoa está editando ao mesmo tempo, os conflitos precisam ser resolvidos de alguma forma sem surpresas desagradáveis.

Os aspectos da avaliação mais relevantes para os usuários finais são:

- **Disponibilidade** — a aplicação precisa funcionar mesmo sem conexão após o primeiro carregamento. Quanto o editor depende de serviços externos para funcionar normalmente?
- **Tolerância a falhas** — o que acontece quando a sessão colaborativa cai? Como o sistema se comporta ao tentar abrir um arquivo corrompido ou quando o armazenamento do navegador está cheio?
- **Recuperabilidade** — os desenhos são salvos automaticamente? É possível retomar o estado anterior depois de fechar a aba por acidente? O desfazer/refazer funciona de forma confiável?
- **Adaptabilidade** — o editor funciona bem em diferentes navegadores, tamanhos de tela e dispositivos de entrada?
- **Substituibilidade** — se o usuário quiser migrar para outra ferramenta, consegue exportar os dados num formato que preserve o conteúdo?

Para os usuários finais, **confiabilidade é a prioridade principal** e portabilidade aparece como aspecto secundário.

## 2. Desenvolvedores do projeto

São as pessoas que trabalham diretamente no código do Excalidraw — seja na aplicação web principal, seja na biblioteca separada (`@excalidraw/excalidraw`). O código é TypeScript com React, organizado em monorepo, o que já coloca algumas exigências de organização que não aparecem em projetos menores.

Para esse grupo, a dificuldade está em escalar o projeto sem perder o controle. Módulos que acumulam responsabilidades demais, dependências cruzadas entre pacotes e falta de cobertura de testes são os tipos de problema que tornam o trabalho de desenvolvimento mais custoso com o tempo.

Os aspectos mais relevantes para quem desenvolve:

- **Modularidade** — os limites entre `excalidraw-app/` e `packages/excalidraw/` estão bem definidos? As dependências seguem uma direção razoável ou há ciclos?
- **Analisabilidade** — a estrutura de diretórios é clara? Os nomes das funções e componentes comunicam o que fazem? Há documentação de arquitetura e convenções?
- **Modificabilidade** — quando alguém muda um componente, quantas outras partes são afetadas? O histórico de pull requests mostra mudanças com alcance previsível ou cheias de surpresas?
- **Testabilidade** — os testes existem, são isolados e cobrem os cenários mais críticos?

Para os desenvolvedores do projeto, **manutenabilidade é a prioridade principal**.

## 3. Mantenedores

Os mantenedores são responsáveis pelo projeto a longo prazo: controlam o que entra no código, gerenciam as versões publicadas, revisam contribuições e garantem que o processo de desenvolvimento não acumule dívida técnica.

Eles têm interesses que se sobrepõem aos dos desenvolvedores, mas com uma perspectiva mais abrangente: não é só sobre o código que vai entrar amanhã, mas sobre se o projeto vai continuar saudável daqui a seis meses.

Os aspectos mais relevantes para os mantenedores:

- **Modularidade e modificabilidade** — mudanças bem contidas são mais fáceis de revisar e têm menos risco de regressão.
- **Testabilidade** — sem testes automatizados e integração contínua bem configurada, revisar contribuições externas vira um trabalho manual enorme.
- **Maturidade** — com que frequência bugs sérios aparecem? O processo de revisão está detectando problemas antes de chegar à produção? As versões publicadas são estáveis?

Para os mantenedores, **manutenabilidade e confiabilidade têm prioridade equivalente**, com portabilidade em papel secundário.

## 4. Contribuidores open source

São desenvolvedores externos que ocasionalmente contribuem com o projeto — corrigindo um bug, adicionando uma funcionalidade pequena ou melhorando a documentação. Eles não conhecem o repositório de cor e precisam conseguir se orientar a partir dos artefatos disponíveis.

A primeira experiência importa muito aqui. Se levar horas para entender onde está o código relevante, configurar o ambiente ou descobrir como rodar os testes, muita gente desiste antes de enviar o pull request.

Os aspectos mais relevantes para contribuidores externos:

- **Analisabilidade** — a estrutura do repositório é intuitiva? Existe um guia de contribuição útil? O lint e o TypeScript ajudam a detectar erros antes de submeter?
- **Instalabilidade** — quais são os pré-requisitos para rodar o projeto localmente? As instruções de instalação funcionam na prática?
- **Testabilidade e modificabilidade** — é fácil reproduzir o cenário que se quer corrigir e verificar que a mudança proposta não quebrou nada?

Para contribuidores open source, **manutenabilidade é a prioridade principal**.

## 5. Desenvolvedores que integram a biblioteca

Esse grupo usa o pacote `@excalidraw/excalidraw` em suas próprias aplicações React. Eles não contribuem com o código do Excalidraw em si — eles dependem dele como uma dependência externa e precisam que essa dependência seja estável, bem documentada e fácil de atualizar.

É um perfil bem diferente dos grupos anteriores: o que interessa é a interface pública da biblioteca, a política de versionamento e a compatibilidade com o ambiente de cada projeto.

Os aspectos mais relevantes para integradores:

- **Reusabilidade** — a biblioteca realmente funciona de forma desacoplada da aplicação oficial? A API pública é clara e estável?
- **Adaptabilidade** — quais versões de React são suportadas? Funciona com diferentes empacotadores? Há problemas com renderização no servidor (SSR)?
- **Instalabilidade** — é simples instalar, configurar e atualizar a biblioteca?
- **Substituibilidade** — se um projeto precisar trocar de ferramenta, consegue exportar os dados de um formato interoperável?

Para os integradores da biblioteca, **portabilidade é a prioridade principal**.

## 6. Equipes de implantação e operação

São as equipes que constroem, configuram e hospedam o Excalidraw em ambientes próprios — seja usando Docker, seja fazendo o build manual. Podem ser equipes de engenharia de plataforma que querem uma instância interna da ferramenta.

Para esse grupo, o que importa é a previsibilidade: o build precisa funcionar de forma reproduzível em diferentes ambientes, e a configuração não pode ser um mistério.

Os aspectos mais relevantes para equipes de operação:

- **Instalabilidade** — o processo de build está documentado de forma clara? O Dockerfile funciona? Há configurações de ambiente que precisam ser ajustadas?
- **Disponibilidade** — a aplicação funciona offline? Quais recursos externos ela acessa e o que acontece quando eles não estão disponíveis?

Para equipes de implantação, **portabilidade é a prioridade principal** com confiabilidade em papel secundário.

## 7. Equipes de qualidade

As equipes de qualidade — que no contexto deste trabalho é a própria equipe avaliadora — precisam que o software seja avaliável. Isso soa óbvio, mas não é: projetos sem testes, sem histórico de issues ou com código difícil de instrumentar criam barreiras reais para a avaliação.

Os aspectos mais relevantes para equipes de qualidade:

- **Testabilidade** — os testes cobrem os cenários críticos? Estão integrados à CI? Como se simula interação com o editor em canvas nos testes automatizados?
- **Maturidade** — como o projeto trata a qualidade ao longo do tempo? Há rastreabilidade entre defeitos relatados, correções e testes adicionados?

Para equipes de qualidade, **manutenabilidade e confiabilidade têm prioridade equivalente**.

## 8. Equipe avaliadora e docentes

A equipe avaliadora conduz este trabalho como parte de uma atividade acadêmica; os docentes acompanham e orientam o processo. Diferente dos grupos anteriores, nosso interesse não é no produto em si, mas na qualidade e na rastreabilidade da avaliação que estamos produzindo.

O que importa para nós:

- Os requisitos precisam ser específicos e rastreáveis a características e interessados concretos.
- O escopo precisa ser realista — não podemos avaliar o que não temos acesso.
- Os procedimentos precisam ser reproduzíveis e verificáveis.
- A versão do código avaliada precisa ser registrada (commit ou tag).

Os docentes esperam que o trabalho siga as normas da família SQuaRE e que cada decisão seja justificada. A edição da ISO/IEC 25010 a ser usada nas próximas fases será confirmada com o professor antes de definirmos as métricas.

## 9. Comunidade e organizações que adotam o produto

Esse grupo inclui equipes, escolas e organizações que usam o Excalidraw regularmente em reuniões, aulas e documentação técnica. Eles não desenvolvem nem implantam — simplesmente usam.

O que importa para esse grupo é a continuidade: o projeto vai continuar sendo mantido? Os formatos de arquivo vão continuar compatíveis entre versões? Se um dia precisarem migrar para outra ferramenta, vão conseguir levar o conteúdo?

Esse grupo não aparece na matriz de prioridades com valores formais, mas suas preocupações se relacionam com confiabilidade (estabilidade entre versões) e portabilidade (exportação dos dados).

---

## Matriz de prioridades

A tabela abaixo resume as prioridades de cada grupo em relação às três características avaliadas. **Principal** significa que aquela característica atende diretamente os interesses do grupo; **Secundário** indica relevância indireta; **–** indica que a característica não é aplicável ou é muito periférica para o grupo.

| Interessado | Manutenibilidade | Confiabilidade | Portabilidade |
|---|---|---|---|
| Usuários finais | – | Principal | Secundário |
| Desenvolvedores do projeto | Principal | Secundário | – |
| Mantenedores | Principal | Principal | Secundário |
| Contribuidores open source | Principal | Secundário | Secundário |
| Desenvolvedores que integram a biblioteca | Secundário | Secundário | Principal |
| Equipes de implantação e operação | – | Secundário | Principal |
| Equipes de qualidade | Principal | Principal | Secundário |

A equipe avaliadora/docentes e a comunidade adotante têm interesses transversais e não entram nessa classificação formal.

---

## Rastreabilidade entre interessados e subcaracterísticas

A tabela a seguir mostra, para cada subcaracterística que vamos avaliar, quais grupos são os principais interessados e quais artefatos do repositório servirão como evidência na Fase 02.

| Subcaracterística | Interessados principais | Artefatos relacionados |
|---|---|---|
| Modularidade | Desenvolvedores; mantenedores | `packages/`, `excalidraw-app/`, arquivos de dependências |
| Reusabilidade | Integradores da biblioteca | `packages/excalidraw/`, `examples/`, interface pública |
| Analisabilidade | Contribuidores; desenvolvedores | Diretórios, configurações de TypeScript e lint, documentação |
| Modificabilidade | Desenvolvedores; mantenedores | Código dos pacotes, commits, pull requests |
| Testabilidade | Equipes de qualidade; mantenedores | Arquivos/configurações de teste, `.github/workflows/` |
| Maturidade | Mantenedores; equipes de qualidade | Integração contínua, testes, histórico de issues |
| Disponibilidade | Usuários finais; operação | Configuração de PWA e offline em `excalidraw-app/` |
| Tolerância a falhas | Usuários finais | Código de colaboração e tratamento de erros |
| Recuperabilidade | Usuários finais | Persistência local, importação/exportação `.excalidraw` |
| Adaptabilidade | Usuários finais; integradores | Compatibilidade e dependências declaradas |
| Instalabilidade | Integradores; operação; contribuidores | `package.json`, `Dockerfile`, documentação de instalação |
| Substituibilidade | Usuários finais; integradores | Funcionalidades de importação/exportação |

---

## Histórico de Versões

| Versão | Data | Descrição | Autor(es) | Revisor(es) |
| ------ | ---- | --------- | --------- | ----------- |
| 0.1 | 04/10/2026 | Documento dos possíveis interessados nesse projeto | [Davi Pierre](https://gitlab.com/DaviPierre) | [Gabriel Monteiro](https://github.com/GabrielSMonteiro) |
| 0.2 | 15/10/2026 | Revisão geral e adição de contexto | [Gabriel Monteiro](https://github.com/GabrielSMonteiro) | |
