divisorSumMap = {}

def getProperDivisors(n):
	divisors = set([1])
	for i in xrange(2, int(n**0.5)+1):
		if n % i == 0:
			divisors.add(i)
			divisors.add(n/i)
	return divisors

def getDivisorSum(n):
	if n in divisorSumMap:
		return divisorSumMap[n]
	divSum = sum(getProperDivisors(n))
	divisorSumMap[n] = divSum
	return divSum
		

limit = 10**6
bestSoFar = 0
for start in xrange(2, limit):
	chain = [start]
	chainSet = set(chain)
	for i in xrange(limit):
		next = getDivisorSum(chain[-1])
		chain.append(next)
		if chain[0] == next:
			break
		if next in chainSet:
			chain = []
			break
		chainSet.add(next)
		if next == 1 or next > limit:
			chain = []
			break
	chainLength = len(chain)-1
	if chainLength > bestSoFar:
		bestSoFar = chainLength
		print bestSoFar, chain, min(chain)
		print
