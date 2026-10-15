from bank import value

import pytest

def test_bank():
    assert value('hello') == 0

def test_anyotherh():
    assert value('hey') == 20

def test_noh():
    assert value('boxod') == 100

def test_spacewithnoh():
    assert value('oy, boss') ==100

def test_casesensitivity():
    assert value('hELlo') == 0




