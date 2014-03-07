from fractions import gcd

limit = 1500000
solutions = set()
duplicates = set()
for m in xrange(2, int((limit/2.0)**0.5)):
	for n in xrange(1, m):
		if (m - n) % 2 == 0 or gcd(n, m) != 1:
			continue
		perimeter = 2*m*(m+n)
		multiple = perimeter
		while multiple <= limit:
			if multiple in solutions:
				duplicates.add(multiple)
			solutions.add(multiple)
			multiple += perimeter
print len(solutions - duplicates)

# see http://en.wikipedia.org/wiki/Pythagorean_triple#Generating_a_triple
