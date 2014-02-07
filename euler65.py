def get_seq(n):
	if (n + 1) % 3 == 0:
		return 2 * (n + 1) / 3
	return 1

def calc_e(iter):
	num = 1
	denom = get_seq(iter+1)
	for i in xrange(iter):
		denom, num = denom * get_seq(iter-i) + num, denom
	return (num + denom*2, denom)

print sum(map(int, list(str(calc_e(98)[0]))))
