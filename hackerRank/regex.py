import re

# HTML Links
"""
regex = "<a href=(\"|')(.*?)(\"|').*?>(<.*?>)*(.*?)(<.*?>)*</a>"
links = []
for n in xrange(int(raw_input())):
	match = re.search(regex, raw_input())
	while match:
		links.append(match.group(2,5))
		match = re.search(regex, match.string[match.end():])
for link in links:
	print link[0] + ',' + link[1].strip()
"""

# Java Comments
"""
source = ""
while True:
	try:
		new = raw_input() + "\n"
		if new == "COOL_BOB\n":
			break
		source += new
	except EOFError:
		break
regex = "(//(.*)\n)|(/\*(.|\n)*?\*/)"
comments = []
match = re.search(regex, source)
while match:
	comments.append(match.group(0).strip())
	match = re.search(regex, match.string[match.end():])
for comment in comments:
	for c in comment.split("\n"):
		print c.strip()
"""

# Count Word Occurrences
"""
regex = "[a-zA-Z0-9_]+"
lines = []
for n in xrange(int(raw_input())):
	tokens = []
	match = re.search(regex, raw_input())
	while match:
		tokens.append(match.group(0))	
		match = re.search(regex, match.string[match.end():])
	lines.append(tokens)
for t in xrange(int(raw_input())):
	word = raw_input()
	count = 0
	for line in lines:
		for token in line:
			if word == token:
				count+=1	
	print count
"""

# Domain Names
"""
regex = "https?://(www\.|ww2\.)?(([a-zA-Z0-9\-]+\.)+[a-zA-Z0-9]{2,4})"
domains = set()
for n in xrange(int(raw_input())):
        match = re.search(regex, raw_input().lower())
        while match:
                domains.add(match.group(2))
                match = re.search(regex, match.string[match.end():])
print ';'.join(sorted(domains))
"""

# Programming Language
"""
java_regex = ["import java(.*);", "public static void main", "System\.(out|exit)"]
c_regex = ["#include<(.*)>", "int main()"]
source = ""
while True:
	try:
		new = raw_input()
		if new == "COOL_BOB":
			break
		source += new
	except EOFError:
		break
for java in java_regex:
	if re.search(java, source):
		print "Java"
for c in c_regex:
	if re.search(c, source):
		print "C"
print "Python"
"""

# Email Address
"""
regex = "[A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,4}"
emails = set()
for n in xrange(int(raw_input())):
	line = raw_input()
	match = re.search(regex, line)
	while match:
		emails.add(match.group(0))
		match = re.search(regex, match.string[match.end():])
print ';'.join(sorted(emails))
"""

# Alternate Spellings 2
"""
lines = []
for n in xrange(int(raw_input())):
	lines.append(raw_input())
for test in xrange(int(raw_input())):
	english_word = raw_input()
	american_word = english_word.replace("our", "or")
	regex = "(^(" + american_word + "( |\n)|" + english_word + "( |\n)))|(( |\n)" + american_word + "( |\n)|( |\n)" + english_word + "( |\n))|((( |\n)" + american_word + "|( |\n)" + english_word + ")$)"
	count = 0
	match = re.search(regex, "\n".join(lines))
	while match:
		count+=1
		match = re.search(regex, match.string[match.end():])
	print count
"""

# Alien Username
"""
regex = "^(_|\.)[0-9]+([a-zA-Z]*_?)$"
for test in xrange(int(raw_input())):
	if re.search(regex, raw_input()):
		print "VALID"
	else:
		print "INVALID"
"""

# HTML Tags
"""
tag_regex = "^<[^(>| )]*(>| )"
tag_names = set()
for test in xrange(int(raw_input())):
	html = raw_input()
	match = re.search(tag_regex, html)
	while match:
		tag_names.add(match.group(0)[1:-1])
		match = re.search(tag_regex, match.string[match.end():])
print ';'.join(sorted(tag_names))
"""

# Find Enclosed Substrings
"""
lines = []
for n in xrange(int(raw_input())):
	lines.append(raw_input())
for test in xrange(int(raw_input())):
	value = raw_input()
	regex = "[a-zA-Z0-9_]+" + value + "[a-zA-Z0-9_]"
	count = 0
	match = re.search(regex, "\n".join(lines))
	while match:
		count+=1
		match = re.search(regex, match.string[match.end():])
	print count
"""

# Alternate Spellings
"""
lines = []
for n in xrange(int(raw_input())):
	lines.append(raw_input())
for test in xrange(int(raw_input())):
	american_word = raw_input()
	english_word = american_word[:-2] + "se"
	regex = "(" + american_word + "|" + english_word + ")"
	count = 0
	match = re.search(regex, "\n".join(lines))
	while match:
		count+=1
		match = re.search(regex, match.string[match.end():])
	print count
"""

# HTML Attributes
"""
open_tag_regex = "<[^/][^>]*>"
open_list = []
for test in xrange(int(raw_input())):
	html = raw_input()
	match = re.search(open_tag_regex, html)
	while match:
		open_list.append(match.group(0))
		match = re.search(open_tag_regex, match.string[match.end():])

attr_regex = " [a-zA-Z0-9]+="
tag_name_regex = "^<[^(>| )]*"
tag_attr = {}
for tag in open_list:
	match = re.search(tag_name_regex, tag)
	tag_name = match.group(0)[1:]
	if tag_name not in tag_attr:
		tag_attr[tag_name] = set()
	match = re.search(attr_regex, tag)
	while match:
		tag_attr[tag_name].add(match.group(0)[1:-1])
		match = re.search(attr_regex, match.string[match.end():])

for tag_name in sorted(tag_attr):
	print tag_name + ":" + ','.join(sorted(tag_attr[tag_name]))
"""

# Valid IP Address
"""
num_range_regex = "((\d)|(\d\d)|(1\d\d)|(2[0-4]\d)|(25[0-5]))"
ipv4_regex = "^(" + num_range_regex + "\.){3}" + num_range_regex + "$"
ipv6_regex = "^(([0-9A-Fa-f]){1,4}\:){7}([0-9A-Fa-f]{1,4})$"
tests = int(raw_input())
for test in xrange(tests):
	line = raw_input()
	if re.search(ipv4_regex, line):
		print "IPv4"
	elif re.search(ipv6_regex, line):
		print "IPv6"
	else:
		print "Neither"
"""

# Stack Exchange Scraper
"""
markup = ""
while True:
	try:
		new = raw_input()
		if new == "COOL_BOB":
			break
		markup += new
	except EOFError:
		break
        
id_regex = "questions/(\d+)"
match = re.search(id_regex, markup)
idList = []
while match:
	idList.append(match.group(0)[10:])
	match = re.search(id_regex, match.string[match.end():])

question_regex = "class=\"question-hyperlink\">([^<])*</a>"
match = re.search(question_regex, markup)
questionList = []
while match:
	questionList.append(match.group(0)[27:-4])
	match = re.search(question_regex, match.string[match.end():])

time_regex = "class=\"relativetime\">([^<])*</span>"
match = re.search(time_regex, markup)
timeList = []
while match:
	timeList.append(match.group(0)[21:-7])
	match = re.search(time_regex, match.string[match.end():])

for index in xrange(len(idList)):
	print idList[index] + ";" + questionList[index] + ";" + timeList[index]
"""

# Valid long/lat pairs
"""
tests = int(raw_input())
regex = "^\((\+|\-)?[1-9]\d*(\.\d+)?, (\+|\-)?[1-9]\d*(\.\d+)?\)$"
for test in xrange(tests):
        pos = raw_input()
	x,y = map(float, pos.replace("(","").replace(")","").replace(" ","").replace("+","").split(","))
        if re.search(regex, pos) and x >= -90 and x <= 90 and y >= -180 and y <= 180:
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
start_regex = "^hackerrank"
end_regex = "hackerrank$"
for test in xrange(tests):
	message = raw_input()
	if re.search(start_regex, message) and re.search(end_regex, message):
		print 0
	elif re.search(start_regex, message):
		print 1
	elif re.search(end_regex, message):
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
