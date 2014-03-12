def getDivisors(n):
	divisors = [1]
	for i in xrange(2, int(n**0.5)+1):
		if n % i == 0:
			divisors.append(i)
	return divisors + map(lambda x: n / x, reversed(divisors))

def getSolutionCount(z):
	solutions = set()
	for k in getDivisors(z):
		for m in getDivisors(z//k):
			n = z // (k*m)
			x = k*m*(m+n)
			y = k*n*(m+n)
			if x >= y:
				solutions.add((x,y))
	return len(solutions)

limit = 1000
for n in xrange(10, 10**10, 10):
	if getSolutionCount(n) >= limit:
		print n
		break
