def sqrt_two(iter):
	denom, num = 2, 1
	for i in xrange(iter):
		denom, num = denom * 2 + num, denom
	return (num + denom, denom)

print len(filter(lambda frac: len(str(frac[0])) > len(str(frac[1])), [sqrt_two(n) for n in xrange(1000)]))
