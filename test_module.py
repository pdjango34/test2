def add(a, b):
    return a + b


def test_add1():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_add2():
    assert add(2, 3) != 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0