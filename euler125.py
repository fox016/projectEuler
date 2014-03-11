limit = 10**8
palindromeSums = set()
squares = [n*n for n in xrange(1, int(limit**0.5))]
for start in xrange(len(squares)):
	for end in xrange(start+1, len(squares)):
		n = sum(squares[start:end+1])
		if n > limit:
			break
		if (lambda s: s == s[::-1])(str(n)):
			palindromeSums.add(n)
print sum(palindromeSums)
