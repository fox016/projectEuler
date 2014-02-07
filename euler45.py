"""
def generatePentagonal(max):
	n = 1
	t_n = 1
	while t_n <= max:
		yield t_n
		n+=1
		t_n = n*(3*n-1)/2

def generateHexagonal(max):
	n = 1
	t_n = 1
	while t_n <= max:
		yield t_n
		n+=1
		t_n = n*(2*n-1)

pentagons = set([p for p in generatePentagonal(2000000000)])
hexagons = set([h for h in generateHexagonal(2000000000)])

print pentagons & hexagons
"""

print set(map(lambda n: n*(3*n-1)/2, xrange(166, 32000))) & set(map(lambda n: n*(2*n-1), xrange(144, 32000)))
