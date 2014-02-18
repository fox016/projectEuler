matrix = [map(int, (lines.split(','))) for lines in open('files/82.dat', 'r')]

rightColumn = set()
for row in xrange(len(matrix)):
	rightColumn.add(matrix[row][-1])
print min(rightColumn)
