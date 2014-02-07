def generate_primes(limit):
	yield 2
	yield 3
	i = 5
	while i <= limit:
		if is_prime(i):
			yield i
		i += 2

def is_prime(n):
	if n < 2:
		return False
	if n < 4:
		return True
	if n % 2 == 0 or n % 3 == 0:
		return False
	d = 3
	while d * d <= n:
		if n % d == 0:
			return False
		d += 2
	return True

best = 50000
primes = [p for p in generate_primes(20000)]

for i1 in xrange(len(primes)):
	p1 = primes[i1]
	if p1 * 5 >= best: break
	for i2 in xrange(i1+1, len(primes)):
		p2 = primes[i2]
		if p1 + p2 * 4 >= best: break
		if not (is_prime(int(str(p1) + str(p2))) and is_prime(int(str(p2) + str(p1)))): continue
		for i3 in xrange(i2+1, len(primes)):
			p3 = primes[i3]
			if p1 + p2 + p3 * 3 >= best: break
			if not (is_prime(int(str(p1) + str(p3))) and is_prime(int(str(p3) + str(p1)))): continue
			if not (is_prime(int(str(p2) + str(p3))) and is_prime(int(str(p3) + str(p2)))): continue
			for i4 in xrange(i3+1, len(primes)):
				p4 = primes[i4]
				if p1 + p2 + p3 + p4 * 2 >= best: break
				if not (is_prime(int(str(p1) + str(p4))) and is_prime(int(str(p4) + str(p1)))): continue
				if not (is_prime(int(str(p2) + str(p4))) and is_prime(int(str(p4) + str(p2)))): continue
				if not (is_prime(int(str(p3) + str(p4))) and is_prime(int(str(p4) + str(p3)))): continue
				for i5 in xrange(i4+1, len(primes)):
					p5 = primes[i5]
					if p1 + p2 + p3 + p4 + p5 >= best: break
					if not (is_prime(int(str(p1) + str(p5))) and is_prime(int(str(p5) + str(p1)))): continue
					if not (is_prime(int(str(p2) + str(p5))) and is_prime(int(str(p5) + str(p2)))): continue
					if not (is_prime(int(str(p3) + str(p5))) and is_prime(int(str(p5) + str(p3)))): continue
					if not (is_prime(int(str(p4) + str(p5))) and is_prime(int(str(p5) + str(p4)))): continue
					best = p1 + p2 + p3 + p4 + p5
					print best
print best
