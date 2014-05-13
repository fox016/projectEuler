def rotate_matrix(lines):
	lines = map(lambda line: line.split(","), lines)
	for col in xrange(len(lines)):
		colStr = ""
		for row in reversed(xrange(len(lines))):
			colStr += lines[row][col] + " "
		print colStr[:-1]

lines = ["1,2,3", "4,5,6", "7,8,9"]
rotate_matrix(lines)
