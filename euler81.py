matrix = [map(int, (lines.split(','))) for lines in open('files/81.dat', 'r')]

for row in xrange(len(matrix)):
	for col in xrange(len(matrix[0])):
		if row == 0 and col == 0:
			continue
		elif row == 0:
			matrix[row][col] += matrix[row][col-1]
		elif col == 0:
			matrix[row][col] += matrix[row-1][col]
		else:
			matrix[row][col] += min(matrix[row-1][col], matrix[row][col-1])
print matrix[-1][-1]
