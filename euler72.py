limit = 1000000
phi = range(0, limit+1)
for i in xrange(2, limit+1):
	if phi[i] == i:
		for j in xrange(i, limit+1, i):
			phi[j] = phi[j] / i * (i-1)
print sum(phi[2:])

"""
def phi(n):
	if n in primeSet:
		return n-1
	if n % 1000 == 0: print n
        return int(reduce(lambda a, b: a * b, map(lambda p: (1 - (1 / float(p))), getPrimeFactors(n)), n))

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
                if p > (n/2.0)+1:
                        break
                if n % p == 0:
                        factors.add(p)
        return factors 

limit = 1000000
primes = getPrimesSieve(limit+1)
primeSet = set(primes)

print sum(map(phi, xrange(2, limit+1)))
"""

"""
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

limit = 8
primes = getPrimesSieve(limit+1)

total = 0
for p in primes:
	total += (p-1)
print total
"""

"""
from fractions import gcd

limit = 8

total = 0
done = set()
#for n in xrange(2, limit+1, -1):
for n in xrange(limit, 1, -1):
	new = True
	for d in done:
		if gcd(d, n) != 1:
			new = False
			break
	if new:
		print n
		total += (n-1)
		done.add(n)
print total
"""

"""
fractions = set()
limit = 10000
for den in xrange(2, limit+1):
	for num in xrange(1, den):
		fractions.add(float(num)/den)
print len(fractions)
"""
