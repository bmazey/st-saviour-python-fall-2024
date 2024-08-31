from holiday import monthly_holiday


def test_monthly_holiday():

    # try a non-existent month
    assert monthly_holiday('Snovember') == ''

    # try all twelve months of the year
    assert monthly_holiday('January') == 'New Year\'s Day'
    assert monthly_holiday('February') == 'Valentine\'s Day'
    assert monthly_holiday('March') == 'St. Patrick\'s Day'
    assert monthly_holiday('April') == 'April Fool\'s Day'
    assert monthly_holiday('May') == 'Memorial Day'
    assert monthly_holiday('June') == 'Juneteenth'
    assert monthly_holiday('July') == 'Independence Day'
    assert monthly_holiday('August') == 'International Youth Day'
    assert monthly_holiday('September') == 'Labor Day'
    assert monthly_holiday('October') == 'Halloween'
    assert monthly_holiday('November') == 'Thanksgiving'
    assert monthly_holiday('December') == 'Christmas'
