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

limit = 100
primes = getPrimesSieve(limit)
for target in xrange(10, limit+1):
	table = [1] + [0] * target
	for value in filter(lambda x: x < target, primes):
		for i in range(value, target+1):
			table[i] += table[i - value]
	if table[target] > 5000:
		print target
		break
