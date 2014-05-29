def print_correlation(x, y):
	n = len(x)
	corr = (n * sum(map(lambda a, b: a*b, x, y)) - (sum(x) * sum(y))) / (((n * sum(map(lambda i:i**2, x)) - sum(x)**2)**0.5) * ((n * sum(map(lambda i:i**2, y)) - sum(y)**2)**0.5))
	print("%.2f" % round(corr,2))

n = int(raw_input())
m = []
p = []
c = []
for x in xrange(n):
	data = map(int, raw_input().split("\t"))
	m.append(data[0])
	p.append(data[1])
	c.append(data[2])

print_correlation(m, p)
print_correlation(p, c)
print_correlation(m, c)
