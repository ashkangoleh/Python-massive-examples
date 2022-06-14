import datetime
import pytz
import logging
str_date = '2009-01-011'
int_date = 1231545600
datetime_date = datetime.datetime(2009, 1, 1)
default = "Invalid date input"

def customizeDateToTimestamp(date: int | str | datetime.datetime):
    try:
        str_to_int_date = lambda x: int(datetime.datetime.strptime(x,"%Y-%m-%d").timestamp())
        datetime_to_int_date = lambda x: int(x.timestamp())
        customize_date = lambda x:  str_to_int_date(x) if isinstance(x, str) else (datetime_to_int_date(x) if isinstance(x,datetime.datetime) else x)
        return customize_date(date)
    except Exception as e:
        logging.error(f"{e}")

print(customizeDateToTimestamp(str_date),
customizeDateToTimestamp(int_date),
customizeDateToTimestamp(datetime_date),
)
