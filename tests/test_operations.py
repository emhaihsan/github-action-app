from src.math_operations import add, subtract

def test_add():
    assert add(1, 2) == 3
    assert add(-2, 1) == -1
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(2, 5) == -3
    assert subtract(0, -4) == -4