def containsOrigin(triangle):
	p = [0, 0]
	a = [triangle[0], triangle[1]]
	b = [triangle[2], triangle[3]]
	c = [triangle[4], triangle[5]]
	return getArea(a, b, p) + getArea(a, p, c) + getArea(p, b, c) == getArea(a, b, c)

def getArea(p1, p2, p3):
	return (1.0/2.0) * abs((p1[0] - p3[0]) * (p2[1] - p1[1]) - (p1[0] - p2[0]) * (p3[1] - p1[1]))

print len(filter(containsOrigin, [map(int, line.split(',')) for line in open('files/102.dat', 'r')]))
