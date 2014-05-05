class Node:
	
	def __init__(self, row, col, val):
		self.row = row
		self.col = col
		self.val = val
		self.visited = False

def count_countries(square_map):
	count = 0
	grid = map(lambda row: list(row), square_map)
	for row in xrange(len(grid)):
		for col in xrange(len(grid[row])):
			grid[row][col] = Node(row, col, grid[row][col])
	for row in xrange(len(grid)):
		for col in xrange(len(grid[row])):
			current = grid[row][col]
			if current.visited:
				continue
			visit_node(current, grid)
			count += 1
	print count

def visit_node(node, grid):
	if node.visited:
		return
	node.visited = True
	borders = []
	if node.row+1 < len(grid):
		borders.append(grid[node.row+1][node.col])
	if node.row-1 > -1:
		borders.append(grid[node.row-1][node.col])
	if node.col+1 < len(grid):
		borders.append(grid[node.row][node.col+1])
	if node.col-1 > -1:
		borders.append(grid[node.row][node.col-1])
	for n in borders:
		if n.val == node.val:
			visit_node(n, grid)

square_map = ["11123",
             "12223",
             "32333",
             "11122",
             "22333"]
count_countries(square_map)
