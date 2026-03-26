# Cachorradas Estúdios — Setup e Deploy

## Pré-requisitos

- Python 3 (sem dependências externas — usa apenas `urllib`, `re`, `json`, `os`, `html`)
- Conta no Google Cloud com YouTube Data API v3 habilitada
- Repositório no GitHub com GitHub Pages ativado na branch `main`

## Configurar a YouTube Data API Key

1. Acessar [Google Cloud Console](https://console.cloud.google.com)
2. Criar projeto ou selecionar existente
3. Habilitar **YouTube Data API v3**
4. Criar credencial → **API Key**
5. (Opcional) Restringir a chave a requisições da API do YouTube

## Configurar o GitHub Secret

1. No repositório GitHub: **Settings → Secrets and variables → Actions**
2. Clicar em **New repository secret**
3. Nome: `YOUTUBE_API_KEY`
4. Valor: a API key gerada acima

## Rodar o script localmente

```bash
# Exportar a variável de ambiente
export YOUTUBE_API_KEY="sua-api-key-aqui"

# Rodar a partir da raiz do repositório
cd /Users/pro15/Claude/cachorradas-estudios
python3 scripts/update_content.py
```

O script modifica o `index.html` diretamente (sem criar arquivos temporários).

## Disparar atualização manual no GitHub Actions

1. Acessar o repositório no GitHub
2. Aba **Actions** → workflow **Atualizar Conteúdo YouTube**
3. Clicar **Run workflow** → **Run workflow**

## Como funciona o deploy automático

O GitHub Pages serve automaticamente qualquer push para a branch `main`. O próprio workflow de atualização faz commit+push do `index.html` modificado, o que aciona o deploy. Não há build step — o `index.html` é servido diretamente.

## Adicionar nova série

Para que uma nova série seja detectada automaticamente nos cards de vídeo:

1. Abrir `scripts/update_content.py`
2. Editar a função `detect_series(title)`:

```python
def detect_series(title):
    t = title.upper()
    # ... séries existentes ...
    if 'NOME DA NOVA SÉRIE' in t:
        return ('Label Exibição', 'cat-blue', 't-blue')  # ajustar cores
    return ('Vídeo', 'cat-blue', 't-dark')
```

3. Se necessário, adicionar nova classe CSS de tema no `index.html` (ver classes `t-blue`, `t-mag`, `t-mix`)

## Estrutura de arquivos

```
cachorradas-estudios/
├── .github/
│   └── workflows/
│       └── update-content.yml   ← agendamento e automação
├── scripts/
│   └── update_content.py        ← script Python de atualização
├── imgs/                        ← assets de mídia (logo, vídeo BG)
├── index.html                   ← site completo (atualizado pelo script)
└── _info/                       ← documentação do projeto
```

## Cota da YouTube Data API v3

A API tem cota de **10.000 unidades/dia** na camada gratuita. O script usa:
- `channels.list` → 1 unidade
- `search.list` → 100 unidades
- `videos.list` → 1 unidade

**Total por execução: ~102 unidades/dia** — bem dentro do limite gratuito.
