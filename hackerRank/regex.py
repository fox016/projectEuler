import re

# Valid long/lat pairs
"""
tests = int(raw_input())
posRegex = "^\((\+|\-)?[1-9]\d*(\.\d+)?, (\+|\-)?[1-9]\d*(\.\d+)?\)$"
for test in xrange(tests):
        pos = raw_input()
	x,y = map(float, pos.replace("(","").replace(")","").replace(" ","").replace("+","").split(","))
        if re.search(posRegex, pos) and x >= -90 and x <= 90 and y >= -180 and y <= 180:
                print "Valid"
        else:
                print "Invalid"
"""

# Hackerrank tweets
"""
tests = int(raw_input())
regex = "hackerrank"
count = 0
for test in xrange(tests):
	tweet = raw_input().lower()
	if re.search(regex, tweet, re.IGNORECASE):
		count+=1
print count
"""

# Find hackerrank
"""
tests = int(raw_input())
startRegex = "^hackerrank"
endRegex = "hackerrank$"
for test in xrange(tests):
	message = raw_input()
	if re.search(startRegex, message) and re.search(endRegex, message):
		print 0
	elif re.search(startRegex, message):
		print 1
	elif re.search(endRegex, message):
		print 2
	else:
		print -1
"""

# Phone number split
"""
tests = int(raw_input())
regex = "(\d{1,10})"
for test in xrange(tests):
	phone = raw_input()
	parts = re.split(regex, phone)
	print "CountryCode=" + parts[1] + ",LocalAreaCode=" + parts[3] + ",Number=" + parts[5]
"""

# Valid PAN format
"""
tests = int(raw_input())
regex = "^([A-Z]{5})(\d{4})([A-Z])$"
for test in xrange(tests):
	pan = raw_input()
	if re.search(regex, pan):
		print "YES"
	else:
		print "NO"
"""

# Valid ID number
"""
t = int(raw_input())
regex = "^([a-z]{0,3})(\d{2,8})([A-Z]{3,})$"
for x in xrange(t):
        id = raw_input()
        if re.search(regex, id):
                print "VALID"   
        else:
                print "INVALID" 
"""
