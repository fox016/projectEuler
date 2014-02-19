from math import floor

def getSequence(n, maxIter):
	whole = int(floor(n**0.5))
	sequence = [whole]
	num = 1
	root = n
	sub = whole
	print "Sub", sub
	for i in xrange(maxIter):
		den = root - (sub**2)	
		print "Den", den
		if den <= 0:
			return sequence
		nextVal = 0
		sub *= num
		print "Sub", sub
		while sub > 0:
			sub -= den
			nextVal+=1
		sequence.append(nextVal)
		print "Next Val", nextVal
		sub = sub * -1	
		print "Sub", sub
		num = den
		print "Num", den
	return sequence

print getSequence(23, 10)
