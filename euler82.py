import sys

matrix = [map(int, (lines.split(','))) for lines in open('files/82.dat', 'r')]
minSet = set()
vertex = [0] * len(matrix)

for row in xrange(len(matrix)):
	vertex[row] = [0] * len(matrix[0])
	for col in xrange(len(matrix[0])):
		vertex[row][col] = {"row" : row, "col" : col, "dist" : sys.maxint}

for startingRow in xrange(len(matrix)):
	vertex[startingRow][0]['dist'] = matrix[startingRow][0]
	queue = list([vertex[startingRow][0]])
	while len(queue) > 0:
		queue = sorted(queue, key = lambda v: v['dist'])
		u = queue.pop(0)
		edges = []
		if u['row']+1 != len(matrix): edges.append(vertex[u['row']+1][u['col']])
		if u['row']-1 != -1: edges.append(vertex[u['row']-1][u['col']])
		if u['col']+1 != len(matrix[0]): edges.append(vertex[u['row']][u['col']+1])
		for edge in edges:
			if edge['dist'] > u['dist'] + matrix[edge['row']][edge['col']]:
				edge['dist'] = u['dist'] + matrix[edge['row']][edge['col']]
				queue.append(edge)

	rightColumn = set()
	for row in xrange(len(vertex)):
		rightColumn.add(vertex[row][-1]['dist'])
	minSet.add(min(rightColumn))

print min(minSet)
