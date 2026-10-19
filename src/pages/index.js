import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';

const team = [
  { name: 'Christopher', github: 'wChrstphr' },
  { name: 'Davi Pierre', github: 'DaviPierre' },
  { name: 'Gabriel Monteiro', github: 'GabrielSMonteiro' },
  { name: 'Letícia de Carvalho', github: 'LeticiaSantosss' },
  { name: 'Luiz Henrique Soares', github: 'luizh-gsoares' },
  { name: 'Maria Eduarda', github: 'eduarda-ogomes' },
];

const docSections = [
  {
    title: 'Fase 01 — Requisitos de Avaliação',
    description: 'Propósito da avaliação, escopo do produto, partes interessadas e modelo de qualidade ISO/IEC 25010:2023.',
    link: '/docs/fase-01/visao-geral',
  },
  {
    title: 'Fase 02 — Especificação da Avaliação',
    description: 'Método GQM, objetivos de medição, abstraction sheets, métricas e critérios de julgamento.',
    link: '/docs/fase-02/visao-geral',
    badge: 'Fase atual',
  },
  {
    title: 'Introdução e Visão Geral',
    description: 'Contexto do projeto, motivações da escolha do Excalidraw e fases da avaliação.',
    link: '/docs/intro',
  },
  {
    title: 'Repositório do Excalidraw',
    description: 'Código-fonte no GitHub da ferramenta de desenho e pacotes da comunidade.',
    externalLink: 'https://github.com/excalidraw/excalidraw',
    isExternal: true,
  },
];

const qualityFocus = [
  {
    title: 'Manutenibilidade',
    description: 'Avaliação da modularidade, facilidade de alteração do código, reusabilidade e cobertura de testes.',
  },
  {
    title: 'Confiabilidade',
    description: 'Análise de maturidade, disponibilidade da aplicação e tolerância a erros e falhas.',
  },
  {
    title: 'Portabilidade',
    description: 'Verificação do funcionamento em diferentes navegadores e facilidade de instalação e execução.',
  },
];

export default function Home() {
  const { siteConfig } = useDocusaurusContext();

  return (
    <Layout
      title="Início"
      description="Documentação de Qualidade de Software do Excalidraw — Grupo Karen Jones, FCTE/UnB"
    >
      <header className="hero-section">
        <div className="hero-inner">
          <p className="hero-context">Qualidade de Software 1 · FCTE / UnB</p>
          <h1 className="hero-title">
            Avaliação de Qualidade do Excalidraw
          </h1>
          <p className="hero-description">
            Documentação do projeto de avaliação do software Excalidraw, desenvolvido pelo Grupo Karen Jones
            com base nas normas da família ISO/IEC 25000 (SQuaRE).
          </p>
          <div className="hero-buttons">
            <Link className="btn btn-primary" to="/docs/intro">
              Ver documentação
            </Link>
            <Link className="btn btn-ghost" href="https://github.com/excalidraw/excalidraw">
              Excalidraw no GitHub
            </Link>
          </div>
        </div>
      </header>

      <main className="content-container">
        <section className="section-block">
          <h2 className="section-title">Documentação</h2>
          <div className="cards-grid">
            {docSections.map((item, idx) => (
              item.isExternal ? (
                <a
                  key={idx}
                  className="doc-card"
                  href={item.externalLink}
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  <div className="doc-card-header">
                    <h3>{item.title}</h3>
                    <span className="card-external-arrow">↗</span>
                  </div>
                  <p>{item.description}</p>
                </a>
              ) : (
                <Link key={idx} className="doc-card" to={item.link}>
                  <div className="doc-card-header">
                    <h3>{item.title}</h3>
                    {item.badge && <span className="card-badge">{item.badge}</span>}
                  </div>
                  <p>{item.description}</p>
                </Link>
              )
            ))}
          </div>
        </section>

        <section className="section-block">
          <h2 className="section-title">Características avaliadas</h2>
          <div className="cards-grid">
            {qualityFocus.map((item, idx) => (
              <div key={idx} className="info-card">
                <h3>{item.title}</h3>
                <p>{item.description}</p>
              </div>
            ))}
          </div>
        </section>

        <section className="section-block">
          <h2 className="section-title">Equipe (Grupo Karen Jones)</h2>
          <div className="team-simple-grid">
            {team.map((member, idx) => (
              <a
                key={idx}
                className="team-simple-item"
                href={`https://github.com/${member.github}`}
                target="_blank"
                rel="noopener noreferrer"
              >
                <span className="team-name">{member.name}</span>
                <span className="team-handle">@{member.github}</span>
              </a>
            ))}
          </div>
        </section>
      </main>
    </Layout>
  );
}
