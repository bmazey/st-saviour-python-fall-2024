import fibonacci

def test_sequence():
    assert fibonacci.sequence(0) == 0
    assert fibonacci.sequence(1) == 1
    assert fibonacci.sequence(2) == 1
    assert fibonacci.sequence(3) == 2
    assert fibonacci.sequence(4) == 3
    assert fibonacci.sequence(5) == 5
    assert fibonacci.sequence(6) == 8
