from rounder import round

def test_rounder():
    # ensure that any floating decimal >= .5 gets rounded up
    assert round(0) == 0
    assert round(.5) == 1

    # ensure the round down requiremnets
    assert round(1.0) == 1
    assert round(1.2) == 1

    # ensure the negative number requirements
    assert round(7.6) == 8
    assert round(7.9) == 8
up]=[]