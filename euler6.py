sum = 0
sum_of_square = 0
for n in xrange(1, 101):
	sum += n
	sum_of_square += n**2
print sum**2 - sum_of_square
