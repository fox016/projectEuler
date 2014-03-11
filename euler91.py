margin = 10**(-5)
limit = 50
total = 0
for x1 in xrange(0, limit+1):
	for y1 in xrange(0, limit+1):
		for x2 in xrange(0, limit+1):
			for y2 in xrange(0, limit+1):
				if (x1, y1) == (0, 0):
					continue
				if (x2, y2) == (0, 0):
					continue
				if (x2, y2) == (x1, y1):
					continue
				lengths = []
				lengths.append(((x1-x2)**2 + (y1-y2)**2)**0.5)
				lengths.append(((x1-0)**2 + (y1-0)**2)**0.5)
				lengths.append(((x2-0)**2 + (y2-0)**2)**0.5)
				lengths = sorted(lengths)
				squares = map(lambda x: x*x, lengths)
				if squares[0] + squares[1] >= squares[2] - margin and squares[0] + squares[1] <= squares[2] + margin:
					total+=1
print total/2
