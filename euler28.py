def sumDiagonal(n):
	sum = 1
	for i in xrange(3, n+1, 2):
		square = i**2
		sum += square + square - (i-1) + square - 2*(i-1) + square - 3*(i-1)
	return sum

print sumDiagonal(1001)
