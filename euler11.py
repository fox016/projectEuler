grid = [map(int, line.split()) for line in open("files/11.dat", 'r')]

highest = 0
for row in xrange(0, 20):
	for col in xrange(0, 20):

		down = 0
		right = 0
		down_right = 0
		up_right = 0

		if(row+3 < 20):
			down = grid[row][col] * grid[row+1][col] * grid[row+2][col] * grid[row+3][col]	
		if(col+3 < 20):
			right = grid[row][col] * grid[row][col+1] * grid[row][col+2] * grid[row][col+3]	
		if(row+3 < 20 and col+3 < 20):
			down_right = grid[row][col] * grid[row+1][col+1] * grid[row+2][col+2] * grid[row+3][col+3]	
		if(col+3 < 20 and row-3 >= 0):
			up_right = grid[row][col] * grid[row-1][col+1] * grid[row-2][col+2] * grid[row-3][col+3]

		best = max(down, right, down_right, up_right)
		if(best > highest):
			highest = best
print highest
