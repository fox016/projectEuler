def getPrimeFactors(n):
	factors = []
	d = 2
	while d * d <= n:
		while n % d == 0:
			if d not in factors:
				factors.append(d)
			n /= d
		d += 1
	if n > 1:
		factors.append(n)
	return factors

n = 1000
while True:
	correct = True
	for i in xrange(0, 4):
		if len(getPrimeFactors(n+i)) != 4:
			correct = False
			break
	if correct:
		print n
		break
	n += 1
