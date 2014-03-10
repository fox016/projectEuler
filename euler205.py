peterDice = range(1,4+1)
colinDice = range(1,6+1)

peterProb = {}
colinProb = {}
for i in xrange(36+1):
	peterProb[i] = 0
	colinProb[i] = 0

for p1 in peterDice:
	for p2 in peterDice:
		for p3 in peterDice:
			for p4 in peterDice:
				for p5 in peterDice:
					for p6 in peterDice:
						for p7 in peterDice:
							for p8 in peterDice:
								for p9 in peterDice:
									peterProb[p1+p2+p3+p4+p5+p6+p7+p8+p9] += 1
for c1 in colinDice:
	for c2 in colinDice:
		for c3 in colinDice:
			for c4 in colinDice:
				for c5 in colinDice:
					for c6 in colinDice:
						colinProb[c1+c2+c3+c4+c5+c6] += 1

solution = 1
for cValue in xrange(36+1):
	colinChance = colinProb[cValue] / 6.0**6.0
	peterChance = 0
	for pValue in xrange(cValue+1):
		peterChance += (peterProb[pValue] / 4.0**9.0)
	solution -= (colinChance * peterChance)
print solution
