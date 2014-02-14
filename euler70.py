def isPermutation(n1, n2):
	return sorted(list(str(n1))) == sorted(list(str(n2)))

def getPrimesSieve(limit):
	notPrimes = [False] * limit
	primes = []
	for i in range(2, limit):
		if notPrimes[i]:
			continue
		for f in xrange(i*2, limit, i):
			notPrimes[f] = True
		primes.append(i)
	return primes

bestN, minRatio = 0, 2.0
primes = filter(lambda n: n > 2000, getPrimesSieve(5000))
for i in xrange(len(primes)):
	for j in xrange(i+1, len(primes)):
		n = primes[i] * primes[j];
		if n > 10000000:
			break
		phiN = (primes[i] - 1) * (primes[j] - 1)
		if isPermutation(n, phiN):
			ratio = float(n) / phiN
			if ratio < minRatio:
				bestN, minRatio = n, ratio
				print bestN, phiN, minRatio
