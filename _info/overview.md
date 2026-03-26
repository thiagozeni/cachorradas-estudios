# Cachorradas Estúdios — Visão Geral

## O que é

Site oficial do canal do YouTube **Cachorradas Estúdios**. Página estática com design dark/neon que exibe estatísticas do canal e os últimos vídeos publicados, atualizados automaticamente todo dia via GitHub Actions.

## Canal YouTube

- **Handle:** `@CachorradasEstudios`
- **ID:** `UC74jUA0r_v3fbYp-07VD7dg`
- **Link:** https://www.youtube.com/@CachorradasEstudios

## Site

- **URL:** https://thiagozeni.github.io/cachorradas-estudios
- **Repositório:** https://github.com/thiagozeni/cachorradas-estudios
- **Hospedagem:** GitHub Pages (deploy automático via push no `main`)

## Atualização automática

Todo dia às **08:00 BRT** (11:00 UTC), um GitHub Actions:
1. Busca stats atuais do canal via YouTube Data API v3
2. Busca os 5 vídeos mais recentes
3. Gera o HTML dos cards de vídeo
4. Substitui os blocos `STATS` e `VIDEOS` no `index.html`
5. Faz commit automático se houve mudança

## Séries ativas

| Série | Cor | Detecção no título |
|---|---|---|
| GDV — Guerra dos Diamantes Vivos | Magenta | `GUERRA DOS DIAMANTE` ou `GDV` |
| Metallica Slayer | Azul | `METALLICA SLAYER` |
| E SE??? | Mix/Experimental | `E SE` |

## Status

Ativo e atualizado automaticamente. Estatísticas atuais (12/03/2026):
- 43 inscritos
- 10 vídeos publicados
- +488 visualizações
