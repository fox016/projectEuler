highest = 0
for i in xrange(100, 1000):
	for j in xrange(100, 1000):
		if((i*j) > highest):
			product = str(i * j)
			if(product == product[::-1]):
				highest = i*j
				print "{0}, {1} => {2}".format(i, j, product)
print "Highest: {0}".format(highest)
