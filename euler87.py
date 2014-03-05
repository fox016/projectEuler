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

limit = 50000000
aList = getPrimesSieve(int(limit**(1/2.0)+1))
bList = filter(lambda x: x <= int(limit**(1/3.0)+1), aList)
cList = filter(lambda x: x <= int(limit**(1/4.0)+1), bList)

sums = set()
for a in aList:
	for b in bList:
		for c in cList:
			sums.add(a**2 + b**3 + c**4)
print len(filter(lambda x: x < limit, sums))
