def minimum_coins(v, e):
	table = [[[0]]] + [[[]]] * e
	for value in v:
		for i in xrange(value, e+1):
			newSolutions = []
			for currentSolutions in table[i]:
				if currentSolutions:
					newSolutions.append(currentSolutions)
			for pastSolutions in table[i-value]:
				if pastSolutions:
					newSolutions.append(list(pastSolutions))
					newSolutions[len(newSolutions)-1].append(value)
			table[i] = newSolutions
	print len(min(table[e], key = lambda t: len(t))) - 1

v = [2, 3, 4]
e = 9
minimum_coins(v, e)
