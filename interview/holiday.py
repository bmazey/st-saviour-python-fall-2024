

def monthly_holiday(month: str) -> str:
    """
    monthly_holiday() accepts a month as an input string and returns:
        - an empty string if the provided month is not valid
        - the correctly formatted holiday string for a given month (see test_holiday.py)
    """

    # TODO implement monthly_holiday function
    if month == 'January':
        return 'New Year\'s Day'
    if month == 'February':
        return 'Valentine\'s Day'
    if month == 'March':
        return 'St. Patrick\'s Day'
    if month == 'April':
        return 'April Fool\'s Day'
    if month == 'May':
        return 'Memorial Day'
    if month == 'June':
        return  'Juneteenth'
    if month == 'July':
        return 'Independence Day'
    if month == 'August':
        return 'International Youth Day'
    if month == 'September':
        return 'Labor Day'
    if month == 'October':
        return 'Halloween'
    if month == 'November':
        return 'Thanksgiving'
    if month == 'December':
        return 'Christmas'
    return ''

