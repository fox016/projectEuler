from fractions import gcd

def phi(n):
	return int(reduce(lambda a, b: a * b, map(lambda p: (1 - (1 / float(p))), getPrimeFactors(n)), n))

def isPermutation(n1, n2):
	return sorted(list(str(n1))) == sorted(list(str(n2)))

def primes_sieve(limit):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []
    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in xrange(i*2, limitn, i):
            not_prime[f] = True

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

primes = primes_sieve(10000000)

bestN, minRatio = 0, 100
for n in xrange(9700000, 10000000):
	print n
	phiN = phi(n)
	if isPermutation(n, phiN):
		ratio = float(n) / phiN
		if ratio < minRatio:
			bestN, minRatio = n, ratio
			print bestN, phiN, minRatio

# answer = 9708131
