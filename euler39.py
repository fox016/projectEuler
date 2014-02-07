def countSolutions(p):
	count = 0
	for a in xrange(0, p/2):
		for b in xrange(a, p/2):
			c = p - a - b
			if a**2 + b**2 == c**2:
				count+=1
	return (p, count)

print max(map(countSolutions, xrange(1001)), key=lambda solution: solution[1])
