// @ts-check
import { themes as prismThemes } from 'prism-react-renderer';

const siteVersion = '1.0';
const buildDate = new Date().toLocaleDateString('pt-BR', { timeZone: 'America/Sao_Paulo' });
const repoUrl = 'https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Qualidade Excalidraw',
  tagline: 'Avaliação de Qualidade de Software — Excalidraw',
  favicon: 'img/logo.svg',

  future: {
    v4: true,
  },

  url: 'https://fcte-qualidade-de-software-1.github.io',
  baseUrl: '/2026-2_T02_KAREN_JONES/',

  organizationName: 'FCTE-Qualidade-de-Software-1',
  projectName: '2026-2_T02_KAREN_JONES',

  onBrokenLinks: 'throw',

  i18n: {
    defaultLocale: 'pt-BR',
    locales: ['pt-BR'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          showLastUpdateTime: true,
          showLastUpdateAuthor: true,
          editUrl:
            'https://github.com/FCTE-Qualidade-de-Software-1/2026-2_T02_KAREN_JONES/tree/main/',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      image: 'img/logo.svg',
      colorMode: {
        defaultMode: 'dark',
        respectPrefersColorScheme: true,
      },
      navbar: {
        title: 'Qualidade Excalidraw',
        logo: {
          alt: 'Logo do projeto Qualidade Excalidraw',
          src: 'img/logo.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'tutorialSidebar',
            position: 'left',
            label: 'Documentação',
          },
          {
            href: 'https://excalidraw.com/',
            label: 'Excalidraw',
            position: 'left',
          },
          {
            href: repoUrl,
            label: 'GitHub',
            position: 'right',
          },
          {
            href: `${repoUrl}/releases`,
            label: 'Release',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Documentação',
            items: [
              {
                label: 'Introdução',
                to: '/docs/intro',
              },
              {
                label: 'Fase 01 — Requisitos',
                to: '/docs/fase-01/visao-geral',
              },
              {
                label: 'Fase 02 — Especificação',
                to: '/docs/fase-02/visao-geral',
              },
            ],
          },
          {
            title: 'Links Úteis',
            items: [
              {
                label: 'Excalidraw (Aplicação)',
                href: 'https://excalidraw.com/',
              },
              {
                label: 'Excalidraw (GitHub)',
                href: 'https://github.com/excalidraw/excalidraw',
              },
            ],
          },
          {
            title: 'Projeto',
            items: [
              {
                label: 'Repositório do Grupo',
                href: repoUrl,
              },
              {
                label: 'Releases',
                href: `${repoUrl}/releases`,
              },
            ],
          },
        ],
        copyright: `Grupo Karen Jones · Qualidade de Software 1 · FCTE/UnB<br/>Versão ${siteVersion} · Atualizado em ${buildDate}`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
