"""Atualiza os blocos STATS e VIDEOS do index.html com dados da YouTube Data API.

Rodado diariamente via GitHub Actions. As funções de formatação/render são puras
e importáveis (testes em tests/); toda a parte de rede e I/O vive em main().
"""
import html
import json
import os
import re
import urllib.request

CHANNEL_ID = 'UC74jUA0r_v3fbYp-07VD7dg'
HTML_FILE = 'index.html'


def fetch(url: str) -> dict:
    with urllib.request.urlopen(url) as r:
        return json.loads(r.read())


def fmt_views(n: int | str) -> str:
    n = int(n)
    if n >= 1000:
        return f'+{n // 1000}k'
    return f'+{n}'


def detect_series(title: str) -> tuple[str, str, str]:
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


def badge(idx: int) -> str:
    if idx == 0:
        return '<div class="vcard-badge badge-fire">DESTAQUE</div>'
    if idx == 1:
        return '<div class="vcard-badge badge-new">NOVO</div>'
    return '<div class="vcard-badge badge-hot">SÉRIE</div>'


def thumb_fallback(vid: str) -> str:
    """onerror que troca maxresdefault (ausente em alguns vídeos → 404) por hqdefault.

    hqdefault sempre existe. `this.onerror=null` evita loop caso o fallback falhe.
    """
    return (
        f"this.onerror=null;"
        f"this.src='https://img.youtube.com/vi/{vid}/hqdefault.jpg'"
    )


def video_card(v: dict, idx: int) -> str:
    vid = v['id']
    title = html.escape(v['snippet']['title'])
    cat_label, cat_cls, theme = detect_series(v['snippet']['title'])
    featured = ' featured' if idx == 0 else ''

    return (
        f'    <a class="vcard{featured} {theme}" href="https://www.youtube.com/watch?v={vid}" target="_blank" rel="noopener">\n'
        f'      <div class="vcard-thumb">\n'
        f'        <img src="https://img.youtube.com/vi/{vid}/maxresdefault.jpg" alt="{title}" loading="lazy"\n'
        f'             onerror="{thumb_fallback(vid)}">\n'
        f'        {badge(idx)}\n'
        f'        <div class="play-btn"><span>▶</span></div>\n'
        f'      </div>\n'
        f'      <div class="vcard-info"><span class="vcard-cat {cat_cls}">{cat_label}</span>'
        f'<div class="vcard-title">{title}</div>'
        f'<div class="vcard-meta">Assistir no YouTube</div></div>\n'
        f'    </a>'
    )


def build_stats(subs: str, vids: str, views: str) -> str:
    return (
        '<!-- STATS:START -->\n'
        '<div class="stats-bar">\n'
        f'  <div class="stat-cell"><span class="stat-num blue">{subs}</span><span class="stat-label">Inscritos</span></div>\n'
        f'  <div class="stat-cell"><span class="stat-num magenta">{vids}</span><span class="stat-label">Vídeos</span></div>\n'
        f'  <div class="stat-cell"><span class="stat-num blue">{views}</span><span class="stat-label">Visualizações</span></div>\n'
        '  <div class="stat-cell"><span class="stat-num magenta">3</span><span class="stat-label">Séries</span></div>\n'
        '</div>\n'
        '<!-- STATS:END -->'
    )


def build_videos(videos: list[dict]) -> str:
    cards = '\n'.join(video_card(v, i) for i, v in enumerate(videos))
    return (
        '  <!-- VIDEOS:START -->\n'
        '  <div class="videos-grid">\n'
        f'{cards}\n'
        '  </div>\n'
        '  <!-- VIDEOS:END -->'
    )


def main() -> None:
    api_key = os.environ['YOUTUBE_API_KEY']

    stats = fetch(
        f'https://www.googleapis.com/youtube/v3/channels'
        f'?part=statistics&id={CHANNEL_ID}&key={api_key}'
    )
    st = stats['items'][0]['statistics']
    subs = st['subscriberCount']
    vids = st['videoCount']
    views = fmt_views(st['viewCount'])

    search = fetch(
        f'https://www.googleapis.com/youtube/v3/search'
        f'?part=snippet&channelId={CHANNEL_ID}&maxResults=5&order=date&type=video&key={api_key}'
    )
    video_ids = [i['id']['videoId'] for i in search['items']]

    details = fetch(
        f'https://www.googleapis.com/youtube/v3/videos'
        f'?part=snippet,statistics&id={",".join(video_ids)}&key={api_key}'
    )
    videos = details['items']

    with open(HTML_FILE, encoding='utf-8') as f:
        html_content = f.read()

    html_content = re.sub(
        r'<!-- STATS:START -->.*?<!-- STATS:END -->',
        build_stats(subs, vids, views), html_content, flags=re.DOTALL
    )
    html_content = re.sub(
        r'<!-- VIDEOS:START -->.*?<!-- VIDEOS:END -->',
        build_videos(videos), html_content, flags=re.DOTALL
    )

    with open(HTML_FILE, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f'✓ Stats  → {subs} inscritos | {vids} vídeos | {views} views')
    print(f'✓ Vídeos → {[v["snippet"]["title"] for v in videos]}')


if __name__ == '__main__':
    main()
