import pytest
from um import count

def test_um():
    assert count('meow meow um um heheheheeh hi um hello world') == 3
    assert count('hi lol') == 0
    assert count('um? hello, okay um....') == 2

def test_complex_um():
    assert count('hello mum, you seen the drums?') == 0
    assert count('Um um uM UM') == 4
