p_n_map = {0:1}
def getP(n):
	if n in p_n_map:
		return p_n_map[n]
	iter = 0
	total = 0
	for pent in filter(lambda x: x <= n, pentagons):
		sign = 1 if iter % 4 <= 1 else -1
		total += sign * getP(n - pent)
		iter += 1
	p_n_map[n] = total
	return total

limit = 100000
pentagons = []
for k in xrange(1, limit+1):
	pos = (k * (3 * k - 1) / 2)
	pentagons.append(pos)
	neg = ((-1*k) * (3 * (-1*k) - 1) / 2)
	pentagons.append(neg)
	if neg > limit:
		break

for n in xrange(1, limit+1):
	p_n = getP(n)
	if p_n % 1000000 == 0:
		print n, p_n
		break

# see http://en.wikipedia.org/wiki/Partition_(number_theory)#Partition_function_formulas
