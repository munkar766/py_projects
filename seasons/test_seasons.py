import pytest
from seasons import get_mins

def test_validity():
    with pytest.raises(ValueError):
        get_mins('cat')
    with pytest.raises(ValueError):
        get_mins('12-01-2008')
    with pytest.raises(ValueError):
        get_mins('2008-13-01')

def test_correct():
    assert get_mins('2008-11-19') == 9354240


