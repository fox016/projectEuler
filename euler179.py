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

primeFactorMap = {1:[]}
def getPrimeFactorization(n):
	if n in primeFactorMap:
		return primeFactorMap[n]
	for p in primes:
		if p > int(n**0.5)+1:
			break
		if n % p == 0:
			primeFactorMap[n] = [p] + getPrimeFactorization(n/p)
			return primeFactorMap[n]
	primeFactorMap[n] = [n]
	return [n]

divisorCountMap = {1:0}
def getDivisorCount(n):
	if n in divisorCountMap:
		return divisorCountMap[n]
	factors = getPrimeFactorization(n)
	product = 1
	"""
	factorSet = set(factors)
	for f in factorSet:
		product *= (factors.count(f)+1)	
	"""
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

limit = 10**7
primes = getPrimesSieve(limit)
count = 0
for n in xrange(1, limit):
	if n % 10000 == 0: print n, count
	if getDivisorCount(n) == getDivisorCount(n+1):
		"""
		print n, n+1
		print count
		print divisorCountMap
		print primeFactorMap
		print
		"""
		count +=1
print count

"""
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
