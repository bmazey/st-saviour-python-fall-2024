from seven_eleven import seven_eleven


def test_seven_eleven():
    # should return empty string when not a multiple of either
    assert seven_eleven(3) == ''
    assert seven_eleven(5) == ''

    # should return 'seven' when a multiple of 7
    assert seven_eleven(7) == 'seven'
    assert seven_eleven(14) == 'seven'

    # should return 'eleven' when a multiple of 11
    assert seven_eleven(11) == 'eleven'
    assert seven_eleven(22) == 'eleven'

    # should return 'seveneleven' when a multiple of both
    assert seven_eleven(77) == 'seveneleven'
    assert seven_eleven(154) == 'seveneleven'