
def getCollatzLength(n):
	length = 1
	while(n != 1):
		if(n % 2 == 0):
			n = n/2
		else:
			n = 3 * n + 1
		length +=1
	return length

bestLength = 0
bestSolution = 0
for i in xrange(100000, 1000000):
	length = getCollatzLength(i)
	if(length > bestLength):
		bestLength = length
		bestSolution = i
print bestSolution
print bestLength
		
