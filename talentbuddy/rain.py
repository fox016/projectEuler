"""
def rain(m, heights):
	grid = list()
	for row in xrange(len(heights) / m):
		gridRow = list()
		for col in xrange(m):
			gridRow.append(heights[row * m + col])
		grid.append(gridRow)
	for row in xrange(len(grid)):
		if row == 0 or row == len(grid)-1:
			continue
		for col in xrange(len(grid[row])):
			if col == 0 or col == len(grid[row])-1:
				continue
			print grid[row][col]
"""

"""
def rain(m, heights):
	vol = 0
	rows = len(heights) / m
	cols = m
	dirty = True
	print heights
	while dirty:
		dirty = False
		for index in xrange(len(heights)):
			row = index / m
			col = index % m
			height = heights[index]
			if row == 0 or col == 0 or row == (rows-1) or col == (cols-1):
				continue
			neighbors = [index-m, index+m, index-1, index+1]
			shortestIndex = min(neighbors, key = lambda i: heights[i])
			while heights[shortestIndex] == height:
				neighbors.remove(shortestIndex)
				# TODO
				break
			if heights[shortestIndex] > height:
				vol += (heights[shortestIndex] - height)
				heights[index] += (heights[shortestIndex] - height)
				dirty = True
		print heights
	print vol
"""

m = 6
heights = [3, 3, 4, 4, 4, 2, 3, 1, 3, 2, 1, 4, 7, 3, 1, 6, 4, 1]
rain(m, heights)
