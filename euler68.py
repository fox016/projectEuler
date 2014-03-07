from itertools import permutations

def isMagic(trial):
	return trial[0] + trial[6] + trial[7] == \
		trial[1] + trial[7] + trial[8] == \
		trial[2] + trial[8] + trial[9] == \
		trial[3] + trial[9] + trial[5] == \
		trial[4] + trial[5] + trial[6]

def getSolution(trial):
	lowest = min(trial[0:5])
	for i in xrange(0,5):
		if trial[i] == lowest:
			lowIndex = i
			break
	if lowIndex == 0:
		solution = [0, 6, 7, 1, 7, 8, 2, 8, 9, 3, 9, 5, 4, 5, 6]
	elif lowIndex == 1:
		solution = [1, 7, 8, 2, 8, 9, 3, 9, 5, 4, 5, 6, 0, 6, 7]
	elif lowIndex == 2:
		solution = [2, 8, 9, 3, 9, 5, 4, 5, 6, 0, 6, 7, 1, 7, 8]
	elif lowIndex == 3:
		solution = [3, 9, 5, 4, 5, 6, 0, 6, 7, 1, 7, 8, 2, 8, 9]
	elif lowIndex == 4:
		solution = [4, 5, 6, 0, 6, 7, 1, 7, 8, 2, 8, 9, 3, 9, 5]
	return map(lambda x: str(trial[x]), solution)

limit = 10**16
bestSoFar = 0
for trial in permutations("1234567890"):
	trial = map(int, trial)
	for index, p in enumerate(trial):
		if p == 0:
			trial[index] = 10
			break
	if isMagic(trial):
		solution = int(''.join(getSolution(trial)))
		if solution > bestSoFar and solution < limit:
			bestSoFar = solution
print bestSoFar
