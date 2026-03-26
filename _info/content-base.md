# Cachorradas Estúdios — Base de Conteúdo

## Identidade do canal

**Tagline:** "Conteúdo original, intenso e sem filtro toda semana."
**Proposta:** Um estúdio de conteúdo sem fórmula e sem filtro. Cada vídeo é uma aposta numa ideia corajosa, executada com energia total.

## Séries

### GDV — Guerra dos Diamantes Vivos
- **Cor:** Magenta (`#D81FBF`)
- **Tema CSS:** `t-mag`, categoria `cat-mag`
- **Detecção:** título contém `GUERRA DOS DIAMANTE` ou `GDV`
- **Badge exibido:** `GDV · Série`

### Metallica Slayer
- **Cor:** Azul (`#1E9FE8`)
- **Tema CSS:** `t-blue`, categoria `cat-blue`
- **Detecção:** título contém `METALLICA SLAYER`
- **Badge exibido:** `Metallica Slayer` ou `Metallica Slayer · Ep N` (quando `[EP N]` está no título)

### E SE???
- **Cor:** Mix/Experimental (roxo-azulado, `t-mix`)
- **Tema CSS:** `t-mix`, categoria `cat-mag`
- **Detecção:** título contém `E SE`
- **Badge exibido:** `E SE???` ou `E SE??? · Ep N` (quando `EPISODIO N` está no título)

## Paleta de cores

```css
--blue:    #1E9FE8   /* azul principal */
--magenta: #D81FBF   /* magenta/rosa principal */
--black:   #0A0A0A   /* fundo principal */
--black2:  #111111   /* fundo secundário (stats, videos) */
--black3:  #181818   /* fundo dos cards */
--white:   #F0F0F0   /* texto principal */
--dim:     rgba(255,255,255,0.55)  /* texto secundário */
```

## Tipografia

- **Barlow Condensed** (pesos: 400, 700, 900 + italic 900) — títulos, headings, botões, labels
- **Barlow** (pesos: 300, 400, 600, 700) — texto corrido, parágrafos

Fonte: Google Fonts

## Animações CSS

| Nome | Efeito | Onde |
|---|---|---|
| `scanline` | Linha de varredura vertical azul→magenta | Hero section |
| `glitch` | Distorção/skew no título principal | `hero-h1` (a cada 8s) |
| `energy-flow` | Reflexo brilhante deslizando | `.section-rule` (barra divisória) |
| `shine` | Reflexo nos botões ao hover | `.btn-primary`, `.cta-btn` |
| `grid-bg` | Grid sutil de linhas azuis | Fundo do hero |
| `neon-flicker` | Piscar de néon nos números de stats | `.stat-num` |
| `border-glow` | Glow pulsante na barra de stats | `.stats-bar` |
| `spin` | Rotação dos anéis ao redor do logo | `.hero-ring` |
| `glow-pulse` | Pulso do drop-shadow no logo | `.hero-logo-wrap img` |
| `float` | Flutuação vertical suave do logo | Seção About |
| `marquee` | Ticker/faixa de texto rolando | `.ticker-bar` |

## Seções do site

1. **Nav** — sticky, blur backdrop, links + botão inscrever-se
2. **Hero** — vídeo de fundo, logo animado, título com glitch, 2 CTAs
3. **Stats** — 4 números: Inscritos, Vídeos, Visualizações, Séries (atualizado via API)
4. **Últimos Drops** — grid dos 5 vídeos mais recentes com cards animados (atualizado via API)
5. **Ticker** — faixa rolante com nomes das séries
6. **Sobre** — texto da missão do canal + logo flutuante
7. **CTA** — chamada para inscrição
8. **Footer** — marca + copyright + link YouTube

## Links do canal

- Canal principal: `https://www.youtube.com/@CachorradasEstudios`
- Inscrição: `https://www.youtube.com/@CachorradasEstudios?sub_confirmation=1`
- Shorts: `https://www.youtube.com/@CachorradasEstudios/shorts`
- Todos os vídeos: `https://www.youtube.com/@CachorradasEstudios/videos`
