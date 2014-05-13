def rhythm(n, k):
	lhs = ["1"] * n
	rhs = ["0"] * (k - n)
	while len(rhs) > 1:
		if len(lhs) > len(rhs):
			old_lhs = list(lhs)
			lhs = map(lambda left, right: left + right, lhs[0:len(rhs)], rhs)
			rhs = old_lhs[len(rhs):]
		elif len(lhs) < len(rhs):
			lhs = map(lambda left, right: left + right, lhs, rhs[0:len(lhs)])
			rhs = rhs[len(lhs):]
		else:
			lhs = map(lambda left, right: left + right, lhs, rhs)
			rhs = []
	print ' '.join(''.join(lhs) + ''.join(rhs))
n = 5
k = 13
rhythm(n, k)
