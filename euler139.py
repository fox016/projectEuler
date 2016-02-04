import math
from fractions import gcd

total = 0
limit = 100000000
for m in xrange(1, int(math.sqrt(limit / 2))):
	for n in xrange(1, m):
		if (m-n) % 2 == 0 or gcd(m, n) != 1:
			continue
		a, b, c = m**2-n**2, 2*m*n, m**2+n**2
		if c % (b - a) == 0:
			total += (limit / (a + b + c))
print total
