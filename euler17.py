ones = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}
teens = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen"}
tens = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

def getLastTwo(i):
	while(i >= 100):
		i -= 100
	if(i <= 0):
		return 0
	if(i < 10):
		return len(ones[i])
	if(i < 20):
		return len(teens[i])
	if(i % 10 == 0):
		return len(tens[int(str(i)[0] + "0")])
	return len(tens[int(str(i)[0] + "0")]) + len(ones[int(str(i)[1])])

def getHundreds(i):
	if(i < 100 or i == 1000):
		return 0
	if(i % 100 == 0):
		return len(ones[int(str(i)[0])]) + len("hundred")
	return len(ones[int(str(i)[0])]) + len("hundredand")

def getThousand(i):
	if(i == 1000):
		return len("onethousand")
	return 0

length = 0
for i in xrange(1, 1001):
	length += getLastTwo(i)
	length += getHundreds(i)
	length += getThousand(i)
print length
