def generate_pandigital():
	i = 1
	while True:
		if is_pandigital(i):
			yield i
		i+=1

def is_pandigital(n):
	return sorted(str(n)) == [str(d) for d in xrange(1,len(str(n))+1)]

def is_prime(n):
	if n < 4:
		return n > 1
	if n % 2 == 0 or n % 3 == 0:
		return False
	d = 3
	while d * d <= n:
		if n % d == 0:
			return False
		d += 2
	return True

for p in generate_pandigital():
	if is_prime(p):
		if p == 7652413:
			print p
			break
