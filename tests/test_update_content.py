"""Testes do gerador de cards/stats (scripts/update_content.py).

Importável sem disparar rede: a execução real vive em main() com guard.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'scripts'))

import update_content as uc  # noqa: E402


def test_video_card_tem_fallback_de_thumbnail():
    """Bug: maxresdefault 404 em vídeos sem maxres → precisa cair p/ hqdefault."""
    card = uc.video_card({'id': 'abc12345678', 'snippet': {'title': 'X'}}, 1)
    assert 'maxresdefault.jpg' in card
    assert 'hqdefault.jpg' in card
    assert 'onerror' in card
    # evita loop de erro
    assert 'this.onerror=null' in card


def test_video_card_escapa_titulo():
    card = uc.video_card({'id': 'x', 'snippet': {'title': '<b>&"hack'}}, 1)
    assert '<b>' not in card
    assert '&amp;' in card


def test_featured_apenas_no_primeiro():
    v = {'id': 'x', 'snippet': {'title': 'a'}}
    assert 'featured' in uc.video_card(v, 0)
    assert ' featured' not in uc.video_card(v, 1)


def test_detect_series():
    assert uc.detect_series('Trailer GDV')[2] == 't-mag'
    assert uc.detect_series('METALLICA SLAYER [Ep 3]')[0] == 'Metallica Slayer · Ep 3'
    assert uc.detect_series('E SE??? Episódio 1')[2] == 't-mix'
    assert uc.detect_series('Vídeo aleatório')[2] == 't-dark'


def test_fmt_views():
    assert uc.fmt_views(684) == '+684'
    assert uc.fmt_views(1500) == '+1k'
