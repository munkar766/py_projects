import pytest
from numb3rs import validate

def test_validate():
    assert validate("192.168.1.1") == True
    assert validate("cat") == False
    assert validate("09.93..1.1") == False

def test_range():
    assert validate("1.256.1.1") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False

