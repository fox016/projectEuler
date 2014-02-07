products = set()
for a in xrange(2000):
	for b in xrange(a, 2000):
		numStr = str(a) + str(b) + str(a*b)
		length = len(numStr)
		if length < 9:
			continue
		if length > 9:
			break
		if sorted(numStr) == ['1','2','3','4','5','6','7','8','9']:
			products.add(a*b)
print sum(products)
