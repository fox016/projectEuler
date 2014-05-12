from datetime import *

def precision(date):
    date_format = "%m/%d/%Y %H:%M:%S"
    start_sec = date[-2:]
    if start_sec == "59" and is_leap_second(datetime.strptime(date, date_format)):
        print date[0:-2] + "60"
    else:
        if start_sec == "60":
            date = date[0:-2] + "59"
        dt = datetime.strptime(date, date_format) + timedelta(seconds=1)
        print dt.strftime(date_format)

def is_leap_second(date_obj):
    if date_obj.month == 6:
        if date_obj.day == 30:
            if date_obj.year in [1972, 1981, 1982, 1983, 1985, 1992, 1993, 1994, 1997, 2012]:
                return True
    elif date_obj.month == 12:
        if date_obj.day == 31:
            if date_obj.year in [1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1987, 1989, 1990, 1995, 1998, 2005, 2008]:
                return True
    return False
