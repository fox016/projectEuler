limit = 10**7
divisorCounts = [0] * limit

def calculate(n):
	for i in xrange(1, (n/2)+1):
		for j in xrange(i*2, n, i):
			divisorCounts[j] += 1

calculate(limit)
sum = 1
count = 0
for i in xrange(2, limit-1):
	if divisorCounts[i] == divisorCounts[i+1]:
		count+=1
print count

"""
Attempt #2, took nearly an hour to run

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

limit = 10**7
primeFactorMap = {1:[]}
primeFactorMap.fromkeys(xrange(limit))
def getPrimeFactorization(n):
	if n in primeFactorMap:
		return primeFactorMap[n]
	primeLimit = int(n**0.5)+1
	for p in primes:
		if p > primeLimit:
			break
		if n % p == 0:
			primeFactorMap[n] = [p] + getPrimeFactorization(n/p)
			return primeFactorMap[n]
	primeFactorMap[n] = [n]
	return [n]

divisorCountMap = {1:0}
divisorCountMap.fromkeys(xrange(limit))
def getDivisorCount(n):
	if n in divisorCountMap:
		return divisorCountMap[n]
	factors = getPrimeFactorization(n)
	product = 1
	current = 0
	done = False
	while not done:
		count = 0
		for next in xrange(current, len(factors)):
			if current == len(factors)-1:
				done = True
			if factors[current] == factors[next]:
				count+=1
				if next == len(factors)-1:
					done = True
			else:
				current = next
				break
		product *= (count+1)
	divisorCountMap[n] = product
	return product

primes = getPrimesSieve(limit)
count = 0
for n in xrange(1, limit):
	if n % 10000 == 0: print n, count
	if getDivisorCount(n) == getDivisorCount(n+1):
		count +=1
print count
"""

"""
Attempt #1

divisorMap = {}
def getDivisors(n):
	if n in divisorMap:
		return divisorMap[n]
	divisors = set([1, n])
	for i in xrange(2, int(n**0.5)+1):
		if n % i == 0:
			divisors.add(i)
			divisors.add(n/i)
	divisorMap[n] = len(divisors)
	return divisorMap[n]

limit = 10**7
count = 0
for n in xrange(1, limit):
	if getDivisors(n) == getDivisors(n+1):
		count +=1
print count
"""
