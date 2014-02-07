for i in xrange(7, 1000, 2):
	s = []
	d = 10 % i
	while d not in s:
		s.append(d)
		d = d * 10 % i
	if len(s) == i - 1:
		m = i
print m
