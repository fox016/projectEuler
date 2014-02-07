from datetime import date

print [date(year, month, 1).weekday() for year in xrange(1901, 2001) for month in xrange(1,13)].count(6)
