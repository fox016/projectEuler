class Cell:

	def __init__(self, row, col, square, value):
		self.row = row
		self.col = col
		self.square = square
		self.value = value
		if value == 0:
			self.possibleValues = [True] * Board.size
		else:
			self.possibleValues = [False] * Board.size
			self.possibleValues[value-1] = True

	def copy(self):
		newCell = Cell(self.row, self.col, self.square, self.value)
		newCell.possibleValues = list(self.possibleValues)
		return newCell

	def removePossibleValue(self, value):
		if self.value != 0:
			return False
		if value == 0:
			return False
		self.possibleValues[value-1] = False
		if self.possibleValues.count(True) == 1:
			self.value = self.possibleValues.index(True) + 1
			return True
		if self.possibleValues.count(True) == 0:
			raise Exception("All values false at [" + self.row + "," + self.col + "]")
		return False

	def getPossibleValues(self):
		possible = []
		for index, value in enumerate(self.possibleValues):
			if value == True:
				possible.append(index+1)
		return possible

class Board:

	size = 9

	def __init__(self, values):
		self.cells = [[None for x in xrange(Board.size)] for x in xrange(Board.size)]
		for row in xrange(Board.size):
			for col in xrange(Board.size):
				self.cells[row][col] = Cell(row, col, Board.getSquare(row, col), values[row][col])

	def copy(self):
		newBoard = Board([[0 for x in xrange(Board.size)] for x in xrange(Board.size)])
		for row in xrange(Board.size):
			for col in xrange(Board.size):
				newBoard.cells[row][col] = self.cells[row][col].copy()
		return newBoard

	def displayBoard(self):
		for row in xrange(Board.size):
			line = ""
			for col in xrange(Board.size):
				line += str(self.cells[row][col].value)
			print line
		print

	def solve(self):
		for row in xrange(Board.size):
			for col in xrange(Board.size):
				self.setInitPossibleValues(self.cells[row][col])
		first = self.getFirstUnknown()
		if first != None:
			for possibleValue in first.getPossibleValues():
				self.guess(self, first, possibleValue)
		else:
			self.guess(self, first, -1)

	def isValid(self):
		for row in xrange(Board.size):
			for x in xrange(3):
				if x == 0: cells = self.getRowCells(row)
				elif x == 1: cells = self.getColCells(row)
				else: cells = self.getSquareCells(row)
				for i in xrange(len(cells)):
					for j in xrange(i+1, len(cells)):
						if(cells[i].value == cells[j].value):
							return False
		return True

	def getRowCells(self, index):
		return self.cells[index]

	def getColCells(self, index):
		col = []
		for row in xrange(Board.size):
			col.append(self.cells[row][index])
		return col

	def getSquareCells(self, index):
		square = []
		count = 0
		for row in xrange(Board.size):
			for col in xrange(Board.size):
				if self.getSquare(row, col) == index:
					square.append(self.cells[row][col])
					count+=1
					if count == 9:
						return square
		return square

	def guess(self, board, cell, newValue):
		if cell == None:
			if board.isValid():
				board.displayBoard()
				self.solutionNumber = int(str(board.cells[0][0].value) + str(board.cells[0][1].value) + str(board.cells[0][2].value))
			return
		newBoard = board.copy()
		newCell = newBoard.cells[cell.row][cell.col]
		newCell.value = newValue
		try:
			newBoard.updateRow(newCell.row, newValue)
			newBoard.updateColumn(newCell.col, newValue)
			newBoard.updateSquare(newCell.square, newValue)
		except Exception, e:
			return

		first = newBoard.getFirstUnknown()
		if first != None:
			for possibleValue in first.getPossibleValues():
				self.guess(newBoard, first, possibleValue)
		else:
			self.guess(newBoard, first, -1)

	def getFirstUnknown(self):
		for row in xrange(Board.size):
			for col in xrange(Board.size):
				if self.cells[row][col].value == 0:
					return self.cells[row][col]
		return None

	def setInitPossibleValues(self, cell):
		if cell.value != 0:
			return
		update = False
		for col in xrange(Board.size):
			if cell.removePossibleValue(self.cells[cell.row][col].value):
				update = True
		for row in xrange(Board.size):
			if cell.removePossibleValue(self.cells[row][cell.col].value):
				update = True
		for row in xrange(Board.size):
			for col in xrange(Board.size):
				if self.cells[row][col].square == cell.square:
					if cell.removePossibleValue(self.cells[row][col].value):
						update = True
		if update:
			self.updateRow(cell.row, cell.value)
			self.updateColumn(cell.col, cell.value)
			self.updateSquare(cell.square, cell.value)

	def updateRow(self, row, value):
		for col in xrange(Board.size):
			if self.cells[row][col].removePossibleValue(value):
				self.updateRow(row, self.cells[row][col].value)
				self.updateColumn(col, self.cells[row][col].value)
				self.updateSquare(self.cells[row][col].square, self.cells[row][col].value)

	def updateColumn(self, col, value):
		for row in xrange(Board.size):
			if self.cells[row][col].removePossibleValue(value):
				self.updateRow(row, self.cells[row][col].value)
				self.updateColumn(col, self.cells[row][col].value)
				self.updateSquare(self.cells[row][col].square, self.cells[row][col].value)

	def updateSquare(self, square, value):
		for row in xrange(Board.size):
			for col in xrange(Board.size):
				if self.cells[row][col].square == square:
					if self.cells[row][col].removePossibleValue(value):
						self.updateRow(row, self.cells[row][col].value)
						self.updateColumn(col, self.cells[row][col].value)
						self.updateSquare(self.cells[row][col].square, self.cells[row][col].value)

	def getSolutionNumber(self):
		return self.solutionNumber

	@staticmethod
	def getSquare(row, col):
		if row < 3:
			if col < 3: return 0
			if col < 6: return 1
			return 2
		if row < 6:
			if col < 3: return 3
			if col < 6: return 4
			return 5
		if col < 3: return 6
		if col < 6: return 7
		return 8

values = []
total = 0
for line in open('files/96.dat'):
	if line[:4] == "Grid":
		if len(values) != 0:
			board = Board(values)
			board.solve()	
			total += board.getSolutionNumber()
		values = []
		continue
	values.append(map(int, line.strip()))
board = Board(values)
board.solve()	
total += board.getSolutionNumber()
print total
