

def monthly_holiday(month: str) -> str:
    """
    monthly_holiday() accepts a month as an input string and returns:
        - an empty string if the provided month is not valid
        - the correctly formatted holiday string for a given month (see test_holiday.py)
    """

    # TODO implement monthly_holiday function

    # Holiday to corresponding month dictionary 
    holidays = {
        "January": "New Year's Day",
        "February": "Valentine's Day",
        "March": "St. Patrick's Day",
        "April": "April Fool's Day",
        "May": "Memorial Day", 
        "June": "Juneteenth",
        "July": "Independence Day",
        "August": "International Youth Day",
        "September": "Labor Day",
        "October": "Halloween",
        "November": "Thanksgiving",
        "December": "Christmas"
    }

    # Check if the provided month is in the holidays dictionary
    if month in holidays:
        # If the month is valid, return the corresponding holiday
        return holidays[month]
    else:
        # If the month is not valid, return an empty string
        return ''
