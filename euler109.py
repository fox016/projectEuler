doubles = set([i*2 for i in xrange(1, 20+1)]+[50])
all_scores = sorted(reduce(lambda x,y: x+y, [[i, i*2, i*3] for i in xrange(1, 20+1)], [0,25,50]))

def solve(n):
	count = 0
	for i in xrange(len(all_scores)):
		for j in xrange(i+1):
			if (n - (all_scores[i] + all_scores[j])) in doubles:
				count+=1
	return count

print sum([solve(n) for n in xrange(100)])
