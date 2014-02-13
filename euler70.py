from fractions import gcd

def phi(n):
	return int(reduce(lambda a, b: a * b, map(lambda p: (1 - (1 / float(p))), getPrimeFactors(n)), n))

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

def getPrimeFactors(n):
	factors = set()
	for p in primes:
		if p > n:
			break
		if n % p == 0:
			factors.add(p)
	return factors 

primes = getPrimesSieve(10000000)

bestN, minRatio = 0, 100
for n in xrange(284029, 10000000):
	phiN = phi(n)
	if isPermutation(n, phiN):
		ratio = float(n) / phiN
		if ratio < minRatio:
			bestN, minRatio = n, ratio
			print bestN, phiN, minRatio

# personal = 284029
# answer = 9708131
