from math import sqrt

def sumDivisors(n):
	sum = 1
	for i in xrange(2, int(sqrt(n)+1)):
		if n % i == 0:
			sum += i
			if(n/i != i):
				sum += n/i
	return sum

def isAbundant(n):
	return sumDivisors(n) > n

abundantNumbers = filter(isAbundant, xrange(1,28124))

sums = set([])
for i in xrange(len(abundantNumbers)):
	for j in xrange(i, len(abundantNumbers)):
		sums.add(abundantNumbers[i] + abundantNumbers[j])

nonSums = set(xrange(1,28124)).difference(sums)
print sum(nonSums)
