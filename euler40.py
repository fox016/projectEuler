numStr = ""
for i in xrange(1, 1000001):
	numStr += str(i)
product = 1
index = 1
while index <= 1000000:
	product *= int(numStr[index-1])
	index *= 10
print product
