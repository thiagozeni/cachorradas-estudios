# Cachorradas Estúdios — Decisões Técnicas

## Por que HTML estático e não um framework (React, Next.js, etc.)

O site tem conteúdo simples: uma página, sem estado complexo, sem rotas, sem formulários. Um framework adicionaria build steps, dependências e complexidade de manutenção sem nenhum benefício real. HTML puro carrega mais rápido, funciona sem JavaScript (exceto o menu hamburger), e qualquer pessoa consegue editar.

## Por que GitHub Pages e não Vercel/Netlify

GitHub Pages é gratuito, integrado com o repositório (zero configuração extra), e suficiente para uma página estática sem build. O repositório já estava no GitHub, então não havia razão para adicionar outro serviço.

## Por que atualizar o HTML diretamente e não chamar a API no cliente (browser)

Chamar a API do YouTube direto do browser exporia a API key publicamente no código-fonte — qualquer pessoa poderia roubá-la e consumir a cota. A abordagem atual mantém a key como GitHub Secret (nunca exposta no HTML), roda server-side (no runner do Actions), e entrega o HTML já pronto para o navegador. Também elimina requests de API por visita ao site.

## Por que usar markers de comentário HTML em vez de um arquivo de dados separado

Com markers (`<!-- STATS:START -->...<!-- STATS:END -->`), o script substitui exatamente o bloco correto no HTML existente sem precisar de um template engine, sem arquivos de dados intermediários, e sem step de build. O `index.html` é sempre o arquivo final e legível. O custo é que o HTML precisa manter os markers intactos — não podem ser removidos manualmente.

## Por que Python e não uma GitHub Action pronta do marketplace

As actions prontas de YouTube Stats geralmente formatam os dados de um jeito fixo e oferecem pouca flexibilidade de layout. Com Python customizado temos controle total: detecção de séries por nome, badges específicos por posição, temas de cor por série, e HTML exatamente como queremos.

## Por que cron às 11:00 UTC (08:00 BRT)

Horário em que o canal provavelmente já postou o vídeo da semana (se for publicado à noite/madrugada). Atualizar cedo garante que visitantes ao longo do dia vejam o conteúdo mais recente. Também é fora do horário de pico de uso da API do Google.
