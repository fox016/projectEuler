end1 = set([1])
end89 = set([89])

def makeChain(n):
	if n in end1:
		return 1
	if n in end89:
		return 89
	return makeChain(sum(map(lambda x: int(x)**2, list(str(n)))))

count = 0
for n in xrange(1, 10000000):
	if makeChain(n) == 1:
		end1.add(n)
	elif makeChain(n) == 89:
		end89.add(n)
		count+=1
print count
