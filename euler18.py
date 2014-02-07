fileReader = open("files/18.dat", 'r')
triangle = []
for line in fileReader:
	triangle.append(map(int, line.split()))

totalRows = len(triangle)
bestSum = 0

def traverse(row, col, sum):

	sum += triangle[row][col]

	if row == 0:
		global bestSum
		if sum > bestSum: bestSum = sum
		return

	if col > 0:
		traverse(row-1, col-1, sum)

	if col < len(triangle[row-1]):
		traverse(row-1, col, sum)

for i in xrange(0, totalRows):
	traverse(totalRows-1, i, 0)

print bestSum
	
