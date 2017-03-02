class Cell:

	def __init__(self, row, col, square, value):
		self.row = row
		self.col = col
		self.square = square
		self.value = value
		if value == 0:
			self.possible_values = [True] * Board.size
		else:
			self.possible_values = [False] * Board.size
			self.possible_values[value-1] = True

	def copy(self):
		new_cell = Cell(self.row, self.col, self.square, self.value)
		new_cell.possible_values = list(self.possible_values)
		return new_cell

	def remove_possible_values(self, value):
		if self.value != 0:
			return False
		if value == 0:
			return False
		self.possible_values[value-1] = False
		if self.possible_values.count(True) == 1:
			self.value = self.possible_values.index(True) + 1
			return True
		if self.possible_values.count(True) == 0:
			raise Exception("All values false at [" + self.row + "," + self.col + "]")
		return False

	def get_possible_values(self):
		possible = []
		for index, value in enumerate(self.possible_values):
			if value == True:
				possible.append(index+1)
		return possible

class Board:

	size = 9

	def __init__(self, values):
		self.cells = [[None for x in xrange(Board.size)] for x in xrange(Board.size)]
		for row in xrange(Board.size):
			for col in xrange(Board.size):
				self.cells[row][col] = Cell(row, col, Board.get_square(row, col), values[row][col])

	def copy(self):
		new_board = Board([[0 for x in xrange(Board.size)] for x in xrange(Board.size)])
		for row in xrange(Board.size):
			for col in xrange(Board.size):
				new_board.cells[row][col] = self.cells[row][col].copy()
		return new_board

	def display_board(self):
		for row in xrange(Board.size):
			line = ""
			for col in xrange(Board.size):
				line += str(self.cells[row][col].value)
			print line
		print

	def solve(self):
		for row in xrange(Board.size):
			for col in xrange(Board.size):
				self.set_init_possible_values(self.cells[row][col])
		first = self.get_first_unknown()
		if first != None:
			for possible_value in first.get_possible_values():
				self.guess(self, first, possible_value)
		else:
			self.guess(self, first, -1)

	def is_valid(self):
		for row in xrange(Board.size):
			for x in xrange(3):
				if x == 0: cells = self.get_row_cells(row)
				elif x == 1: cells = self.get_col_cells(row)
				else: cells = self.get_square_cells(row)
				for i in xrange(len(cells)):
					for j in xrange(i+1, len(cells)):
						if(cells[i].value == cells[j].value):
							return False
		return True

	def get_row_cells(self, index):
		return self.cells[index]

	def get_col_cells(self, index):
		col = []
		for row in xrange(Board.size):
			col.append(self.cells[row][index])
		return col

	def get_square_cells(self, index):
		square = []
		count = 0
		for row in xrange(Board.size):
			for col in xrange(Board.size):
				if self.get_square(row, col) == index:
					square.append(self.cells[row][col])
					count+=1
					if count == 9:
						return square
		return square

	def guess(self, board, cell, new_value):
		if cell == None:
			if board.is_valid():
				board.display_board()
				self.solution_number = int(str(board.cells[0][0].value) + str(board.cells[0][1].value) + str(board.cells[0][2].value))
			return
		new_board = board.copy()
		new_cell = new_board.cells[cell.row][cell.col]
		new_cell.value = new_value
		try:
			new_board.update_row(new_cell.row, new_value)
			new_board.update_column(new_cell.col, new_value)
			new_board.update_square(new_cell.square, new_value)
		except Exception, e:
			return

		first = new_board.get_first_unknown()
		if first != None:
			for possible_value in first.get_possible_values():
				self.guess(new_board, first, possible_value)
		else:
			self.guess(new_board, first, -1)

	def get_first_unknown(self):
		for row in xrange(Board.size):
			for col in xrange(Board.size):
				if self.cells[row][col].value == 0:
					return self.cells[row][col]
		return None

	def set_init_possible_values(self, cell):
		if cell.value != 0:
			return
		update = False
		for col in xrange(Board.size):
			if cell.remove_possible_values(self.cells[cell.row][col].value):
				update = True
		for row in xrange(Board.size):
			if cell.remove_possible_values(self.cells[row][cell.col].value):
				update = True
		for row in xrange(Board.size):
			for col in xrange(Board.size):
				if self.cells[row][col].square == cell.square:
					if cell.remove_possible_values(self.cells[row][col].value):
						update = True
		if update:
			self.update_row(cell.row, cell.value)
			self.update_column(cell.col, cell.value)
			self.update_square(cell.square, cell.value)

	def update_row(self, row, value):
		for col in xrange(Board.size):
			if self.cells[row][col].remove_possible_values(value):
				self.update_row(row, self.cells[row][col].value)
				self.update_column(col, self.cells[row][col].value)
				self.update_square(self.cells[row][col].square, self.cells[row][col].value)

	def update_column(self, col, value):
		for row in xrange(Board.size):
			if self.cells[row][col].remove_possible_values(value):
				self.update_row(row, self.cells[row][col].value)
				self.update_column(col, self.cells[row][col].value)
				self.update_square(self.cells[row][col].square, self.cells[row][col].value)

	def update_square(self, square, value):
		for row in xrange(Board.size):
			for col in xrange(Board.size):
				if self.cells[row][col].square == square:
					if self.cells[row][col].remove_possible_values(value):
						self.update_row(row, self.cells[row][col].value)
						self.update_column(col, self.cells[row][col].value)
						self.update_square(self.cells[row][col].square, self.cells[row][col].value)

	def get_solution_number(self):
		return self.solution_number

	@staticmethod
	def get_square(row, col):
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
			total += board.get_solution_number()
		values = []
		continue
	values.append(map(int, line.strip()))
board = Board(values)
board.solve()	
total += board.get_solution_number()
print total
