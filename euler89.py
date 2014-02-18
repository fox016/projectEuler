values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

def toRoman(number):
	roman = ""
	for i in xrange(len(values)):
		while number >= values[i]:
			roman += symbols[i]
			number -= values[i]
	return roman

def toNumber(roman):
	number = 0
	for i in xrange(len(values)):
		sym = symbols[i]
		while roman[0:len(sym)] == sym:
			number += values[i]
			roman = roman[len(sym):]
	return number

romans = [line.strip() for line in open('files/89.dat', 'r')]
startLen = len(''.join(romans))
endLen = len(''.join(map(toRoman, map(toNumber, romans))))
print startLen - endLen
