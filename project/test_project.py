import pytest
from project import valid, win, lose, draw
options = ['rock', 'paper', 'scissors']

def test_valid():
    assert valid('rock', options) == 'rock'
    assert valid('meow', options) == None

def test_win():
    assert win('rock', 'scissors') == 'you won!'
    assert win('paper', 'rock') == 'you won!'

def test_lose():
    assert lose ('paper', 'scissors') == 'you lost!'
    assert lose('rock', 'paper') == 'you lost!'

def test_draw():
    assert draw ('paper', 'paper') == 'its a draw'
    assert draw ('rock', 'rock') == 'its a draw'

