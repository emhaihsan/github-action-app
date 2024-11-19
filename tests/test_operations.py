from src.math_operations import add, subtract, multiply_two, divide, power, modulo

def test_add():
    assert add(1, 2) == 3
    assert add(-2, 1) == -1
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(2, 5) == -3
    assert subtract(0, -4) == -4

def test_multiply_two():
    assert multiply_two(3) == 6
    assert multiply_two(-1) == -2
    assert multiply_two(0) == 0

def test_divide():
    assert divide(6, 2) == 3
    assert divide(5, 2) == 2.5
    assert divide(-4, 2) == -2

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(3, 1) == 3

def test_modulo():
    assert modulo(5, 2) == 1
    assert modulo(4, 2) == 0
    assert modulo(7, 3) == 1
