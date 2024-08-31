from seven_eleven import seven_eleven


def test_seven_eleven():
    assert seven_eleven(3) == ''
    assert seven_eleven(5) == ''
    assert seven_eleven(7) == 'seven'
    assert seven_eleven(11) == 'eleven'
    assert seven_eleven(14) == 'seven'
    assert seven_eleven(22) == 'eleven'
    assert seven_eleven(77) == 'seveneleven'
    assert seven_eleven(154) == 'seveneleven'