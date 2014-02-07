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

diagonals = [1]
inc = 2
primeCount = 0
for iter in xrange(30000):
	for i in xrange(4):
		d = diagonals[-1] + inc
		diagonals.append(d)
		if is_prime(d):
			primeCount+=1
	inc += 2
	if float(primeCount) / float(len(diagonals)) < 0.10:
		print iter*2+3
		break
