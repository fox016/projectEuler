def generateCubes(n):
	while True:
		yield n**3
		n+=1

keyToCubeSet = {}
for cube in generateCubes(345):
	key = ''.join(sorted(str(cube)))
	if key not in keyToCubeSet:
		keyToCubeSet[key] = set()
	keyToCubeSet[key].add(cube)
	if len(keyToCubeSet[key]) == 5:
		print keyToCubeSet[key]
		break
