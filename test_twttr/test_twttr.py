from twttr import shorten
import pytest



def test_upper():
    assert shorten("TWITTER") == 'TWTTR'



def test_lower():
    assert shorten('twitter') == 'twttr'

def test_gap():
    assert shorten('hello, twitter') == 'hll, twttr'

def test_digit():
    assert shorten('meow1234') == 'mw1234'

