from combinatoric import factorial, choose

def test_factorial():
    assert factorial(5) == 120
    assert factorial(3) == 6

def test_choose():
    # TODO implement for +10 bonus
    assert choose(5, 2) == 10