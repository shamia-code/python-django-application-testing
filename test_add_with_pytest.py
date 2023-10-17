import pytest

def add(a,b):
    return a+ b 

@pytest.mark.parametrize('a, b, expected', [
    (2, 2, 4),
    (-2, -2, -4)
])

def test_add(a, b, expected):
    assert add(a, b) == expected





















