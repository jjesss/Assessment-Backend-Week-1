"""Functions for working with dates."""

from datetime import datetime, date


def convert_to_datetime(date_val: str) -> datetime:
    """Converts date_val to datetime"""
    try:
        return datetime.strptime(date_val, "%d.%m.%Y")
    except Exception as err:
        raise ValueError("Unable to convert value to datetime.") from err


def get_days_between(first: datetime, last: datetime) -> int:
    """Gets days between two dates"""
    try:
        return (last-first).days
    except Exception as err:
        raise TypeError("Datetimes required.") from err


def get_day_of_week_on(date_val: datetime) -> str:
    """Returns day of datetime given"""
    try:
        return date_val.strftime("%A")
    except Exception as err:
        raise TypeError("Datetime required.") from err


def get_current_age(birthdate: date) -> int:
    """Gets the current age based on birthdate"""
    try:
        # convert string to datetime
        age = datetime.now().year - birthdate.year
        if age != 0:
            age -= 1
        # if the birthday has passed this year then add 1
        if ((datetime.now().month, datetime.now().day)
            > (birthdate.month,
               birthdate.day)):
            age += 1

        return age
    except Exception as err:
        raise TypeError("Date required.") from err
