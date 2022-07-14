from datetime import datetime


def convert_date_str_to_datetime(date_string):
    if not date_string:
        return None
    try:
        datetime_obj = datetime.strptime(date_string, "%d-%m-%Y %H:%M")
    except ValueError:
        datetime_obj = None
    return datetime_obj