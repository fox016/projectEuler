def generatePentagonals(max):
	n = 1
	p_n = 1
	while p_n <= max:
		yield p_n
		n+=1
		p_n = n * (3 * n - 1) / 2

def isPentagonal(p):
	return ((0.5 + (.25+6*p)**0.5)/3)%1 == 0

pents = [p for p in generatePentagonals(10000000)]

for j in xrange(len(pents)):
	for k in xrange(j+1, len(pents)):
		if isPentagonal(pents[j] + pents[k]) and isPentagonal(pents[k] - pents[j]):
			print pents[k] - pents[j]
