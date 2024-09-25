

def monthly_holiday(month: str) -> str:
    """
    monthly_holiday() accepts a month as an input string and returns:
        - an empty string if the provided month is not valid
        - the correctly formatted holiday string for a given month (see test_holiday.py)
    """

    # TODO implement monthly_holiday function
    
    # returns a specific holiday based on a given month
    if month == "January":
        return "New Year's Day"
    elif month == "February":
        return "Valentine's Day"
    elif month == "March":
        return "St. Patrick's Day"
    elif month == "April":
        return "April Fool's Day"
    elif month == "May":
        return "Memorial Day"
    elif month == "June":
        return "Juneteenth"
    elif month == "July":
        return "Independence Day"
    elif month == "August":
        return "International Youth Day"
    elif month == "September":
        return "Labor Day"
    elif month == "October":
        return "Halloween"
    elif month == "November":
        return "Thanksgiving"
    elif month == "December":
        return "Christmas"
        
    # returns an empty string if the given month doesn't exist
    else:
        return ""