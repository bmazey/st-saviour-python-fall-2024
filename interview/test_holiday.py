from holiday import monthly_holiday


def test_monthly_holiday():

    # try a non-existent month
    assert monthly_holiday('Snovember') == ''

    # try all twelve months of the year
    assert 