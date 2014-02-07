best = 0
for first in xrange(1, 10000):
	for n in xrange(2, 10):
		conProductStr = ''.join([str(first * i) for i in xrange(1,n+1)])
		if ''.join(sorted(conProductStr)) == "123456789":
			if int(conProductStr) > best:
				best = int(conProductStr)
print best

#print max(map(lambda lst: int(''.join(lst)), filter(lambda conProductStr: ''.join(sorted(''.join(conProductStr))) == "123456789", [[str(first * i) for i in xrange(1,n+1)] for n in xrange(2,10) for first in xrange(1, 100000)])))
