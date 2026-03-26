# Cachorradas Estúdios — Arquitetura

## Stack

- **HTML5 + CSS3** — site estático, sem framework
- **Python 3** — script de atualização de conteúdo
- **YouTube Data API v3** — busca stats do canal e lista de vídeos
- **GitHub Actions** — automação do ciclo diário de atualização
- **GitHub Pages** — hospedagem estática gratuita

## Fluxo de atualização

```
GitHub Actions (cron diário 11:00 UTC / 08:00 BRT)
        ↓
scripts/update_content.py
  ├── GET /youtube/v3/channels?part=statistics → subs, vídeos, views
  ├── GET /youtube/v3/search?order=date&maxResults=5 → IDs dos vídeos
  ├── GET /youtube/v3/videos?part=snippet,statistics → detalhes
  ├── detect_series(título) → série + cor + tema
  ├── Gera HTML do bloco STATS (stats-bar)
  └── Gera HTML dos cards VIDEOS (videos-grid)
        ↓
Substituição via regex no index.html
  <!-- STATS:START --> ... <!-- STATS:END -->
  <!-- VIDEOS:START --> ... <!-- VIDEOS:END -->
        ↓
git commit + git push (apenas se index.html mudou)
        ↓
GitHub Pages (deploy automático)
```

## Sistema de markers HTML

O `index.html` contém dois pares de comentários que delimitam blocos substituíveis:

```html
<!-- STATS:START -->
  ... bloco gerado automaticamente ...
<!-- STATS:END -->

<!-- VIDEOS:START -->
  ... cards gerados automaticamente ...
<!-- VIDEOS:END -->
```

O script usa `re.sub` com `re.DOTALL` para substituir tudo entre os markers. O resto do HTML permanece intacto entre atualizações.

## Detecção de séries

```python
def detect_series(title):
    t = title.upper()
    if 'GUERRA DOS DIAMANTE' in t or 'GDV' in t:
        return ('GDV · Série', 'cat-mag', 't-mag')
    if 'METALLICA SLAYER' in t:
        ep = re.search(r'\[EP\s*(\d+)\]', t)
        label = f'Metallica Slayer · Ep {ep.group(1)}' if ep else 'Metallica Slayer'
        return (label, 'cat-blue', 't-blue')
    if 'E SE' in t:
        ep = re.search(r'EPIS[ÓO]DIO\s*(\d+)', t)
        label = f'E SE??? · Ep {ep.group(1)}' if ep else 'E SE???'
        return (label, 'cat-mag', 't-mix')
    return ('Vídeo', 'cat-blue', 't-dark')
```

Retorna: `(label_exibição, classe_categoria, classe_tema_card)`

## Badges dos cards

| Posição | Badge | Estilo |
|---|---|---|
| 0 (mais recente) | DESTAQUE | Gradiente azul→magenta |
| 1 | NOVO | Azul sólido |
| 2–4 | SÉRIE | Magenta sólido |

## GitHub Actions

**Arquivo:** `.github/workflows/update-content.yml`

```yaml
on:
  schedule:
    - cron: '0 11 * * *'   # 08:00 BRT
  workflow_dispatch:         # disparo manual
```

- Runner: `ubuntu-latest`
- Permissões: `contents: write` (para fazer push)
- Secret necessário: `YOUTUBE_API_KEY`
- Commit automático apenas se `index.html` foi modificado

## Google Analytics

Integrado via Google Tag Manager:
- **ID:** `G-GQ2DERV731`
- Script assíncrono no `<head>` do `index.html`

## Assets de mídia

```
imgs/
├── Cachorradas BG Black.mp4    ← vídeo de fundo do hero (opacidade 28%)
├── Cachorradas BG.jpeg         ← fallback/poster do vídeo
├── Cachorradas Logo.jpeg       ← logo principal
├── cachorradas-logo-menu.png   ← logo na nav e footer
├── cachorradas-logo-removebg.png
└── cachorradas-logo-sem-txt.png ← logo sem texto (hero e about)
```
