from math import sqrt

def countDivisors(n):
	if n < 1:
		return 0
	if n == 1:
		return 1
	divisors = 2
	for i in xrange(2, int(sqrt(n)) + 1):
		if n % i == 0:
			divisors += 2
	return divisors

count = 1
triangle = 0
while True:
	triangle += count
	if(countDivisors(triangle) > 500):
		print triangle
		exit(0)
	count += 1
