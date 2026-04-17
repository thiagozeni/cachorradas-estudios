# Cachorradas Estúdios

Site oficial do canal YouTube [**Cachorradas Estúdios**](https://youtube.com/@CachorradasEstudios).

🔗 **URL:** https://thiagozeni.github.io/cachorradas-estudios

## Séries publicadas

- **GDV** — Guerra dos Diamantes Vivos
- **Metallica Slayer**
- **E SE???**

## Stack

- HTML/CSS estático
- Python (script de atualização de conteúdo)
- YouTube Data API v3
- GitHub Actions (automação diária)
- GitHub Pages (hosting)

## Automação

Um workflow do GitHub Actions roda todo dia às **08h BRT** e atualiza as estatísticas do canal + lista de vídeos via YouTube Data API.

- Script: `scripts/update_content.py`
- Workflow: `.github/workflows/update-content.yml`

### Variáveis / Secrets

| Nome | Tipo | Onde |
|---|---|---|
| `YOUTUBE_API_KEY` | Secret | GitHub repo → Settings → Secrets → Actions |

**Canal ID:** `UC74jUA0r_v3fbYp-07VD7dg`

## Deploy

GitHub Pages automático ao push em `main`. Sem build step.

```bash
git push origin main   # publicado em ~1min
```

## Desenvolvimento local

Como é HTML estático, qualquer servidor funciona:

```bash
python3 -m http.server 8000
# http://localhost:8000
```
