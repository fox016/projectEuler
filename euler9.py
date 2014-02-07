for a in xrange(0, 400):
	for b in xrange(a, 400):
		c = 1000 - a - b
		if a**2 + b**2 == c**2:
			print (a * b * c)
			exit(0)
