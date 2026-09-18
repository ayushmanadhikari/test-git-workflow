# test_calculator.py
from calculator import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_sub():
    assert sub(1,2) == 2
