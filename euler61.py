def generatePolygon(limit, function):
	n = 1
	t = 1
	while t <= limit:
		yield t
		n += 1
		t = function(n)

def getCycle(start, indices, solution):
	global polys
	if len(indices) == 0:
		if str(solution[0])[0:2] == str(solution[-1])[-2:]:
			print solution
			print sum(solution)
			exit(0)
		return
	for i in indices:
		for j in xrange(len(polys[i])):
			if polys[i][j] >= ((start%100) * 100) and polys[i][j] < ((start%100)+1) * 100:
				iCopy = list(indices)
				iCopy.remove(i)
				sCopy = list(solution)
				sCopy.append(polys[i][j])
				getCycle(polys[i][j], iCopy, sCopy)

polys = list()
polys.append([p for p in generatePolygon(10000, lambda n: n*(n+1)/2) if p >= 1000])	# Triangles
polys.append([p for p in generatePolygon(10000, lambda n: n**2) if p >= 1000])		# Squares
polys.append([p for p in generatePolygon(10000, lambda n: n*(3*n-1)/2) if p >= 1000])	# Pentagons
polys.append([p for p in generatePolygon(10000, lambda n: n*(2*n-1)) if p >= 1000])	# Hexagons
polys.append([p for p in generatePolygon(10000, lambda n: n*(5*n-3)/2) if p >= 1000])	# Heptagons
polys.append([p for p in generatePolygon(10000, lambda n: n*(3*n-2)) if p >= 1000])	# Octagons

for i in xrange(len(polys)):
	for j in xrange(len(polys[i])):
		getCycle(polys[i][j], [n for n in xrange(len(polys)) if n != i], [polys[i][j]])
