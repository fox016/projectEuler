class Board:

	def __init__(self, values):
		self.cells = values

	def solve(self):
		pass

	def getSolutionNumber(self):
		return int(''.join(map(str, self.cells[0][:3])))

values = None
total = 0
for line in open('files/96.dat'):
	if line[:4] == "Grid":
		if values != None:
			board = Board(values)
			board.solve()	
			total += board.getSolutionNumber()
		values = []
		continue
	values.append(map(int, line.strip()))
print total
