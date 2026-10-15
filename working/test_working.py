import pytest
from working import convert

def test_convert_string():
    with pytest.raises(ValueError):
        convert('cat')
    with pytest.raises(ValueError):
        convert('meow')

def test_convert_to():
    with pytest.raises(ValueError):
        convert('5 AM - 9 PM') 

def test_correct():
    assert convert('9:35 AM to 9:50 PM') == '09:35 to 21:50'
