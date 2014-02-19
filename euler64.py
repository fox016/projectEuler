"""
from math import floor

def getSequence(n, maxIter):

	whole = int(floor(n**0.5))
	sequence = [whole]
	num = 1
	sub = whole
	targetSub = whole * -1

	for i in xrange(maxIter):

		den = (n - (sub**2)) / num
		if den <= 0:
			return sequence

		nextVal = 0
		while sub >= targetSub:
			sub -= den
			nextVal+=1
		sub += den
		nextVal-=1

		sequence.append(nextVal)
		sub = sub * -1	
		num = den

	return sequence

def getPeriodLength(sequence):
	if len(sequence) == 0:
		return 0
	for length in xrange(1, len(sequence)):
		pattern = sequence[0:length]
		correctLength = True
		for startPos in xrange(0, len(sequence), len(pattern)):
			portion = sequence[startPos:startPos+len(pattern)]
			if (pattern != portion) and (len(portion) == len(pattern)):
				correctLength = False
				break
		if correctLength:
			return length
		

limit = 10000
maxPeriodLen = 450
count = 0
for n in xrange(2, limit+1):
	periodLength = getPeriodLength(getSequence(n, maxPeriodLen)[1:])
	if periodLength % 2 == 1:
		count+=1
print count
"""

import math
   
def getPeriodLength(n):
	num = 0
	den = 1
	wholeRoot = math.floor(math.sqrt(n))
	sub = wholeRoot
	iter = 0
	while sub != wholeRoot * 2:
		num = den * sub - num
		den = (n - num**2) / den
		if den == 0:
			return 0
		sub = math.floor((wholeRoot + num) / den)
		iter+=1
	return iter

print len(filter(lambda n: n % 2 == 1, map(getPeriodLength, xrange(2, 10000+1))))
