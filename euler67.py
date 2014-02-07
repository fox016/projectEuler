triangle = [map(int, line.split()) for line in open("files/67.dat", 'r')]

rows = len(triangle) + 1

table = [0] * rows
for i in xrange(0, rows):
	table[i] = [0] * rows

table[1][1] = triangle[0][0]
for i in xrange(2, rows):
	for j in xrange(1, i+1):
		table[i][j] = triangle[i-1][j-1] + max(table[i-1][j], table[i-1][j-1])

print max(table[-1])
