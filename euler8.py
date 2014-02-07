longNumber = [line for line in open('files/8.dat', 'r')][0]

highest = 0
for i in xrange(0, len(longNumber) - 5):
	five = longNumber[i:i+5]
	product = 1
	for digit in five:
		product *= int(digit)
	if(product > highest):
		highest = product
print highest
