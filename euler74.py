from math import factorial
from itertools import permutations

def getNonRepeatChain(n):
	chain = set()
	while n not in chain:
		chain.add(n)
		if len(chain) > 60:
			return 61
		n = sum(map(factorial, map(int, list(str(n)))))
	return len(chain)

def countPermutations(numStr, length):
        count = len(filter(lambda n: len(str(n)) == length, set([int("".join(p)) for p in permutations(numStr)])))
	if "1" in numStr:
		count += countPermutations(numStr.replace("1", "0"), length)
	return count

count = 0

for n in xrange(1000, 10000):
	if getNonRepeatChain(n) == 60:
		count += countPermutations(str(n), len(str(n)))
		print count
		break

for n in xrange(100000, 1000000):
	if getNonRepeatChain(n) == 60:
		count += countPermutations(str(n), len(str(n)))
		print count
		break

print count
