class Board:

	def __init__(self, boardStr):
		self.whiteSet = set()
		self.blackSet = set()
		self.rows = 8
		self.cols = 8
		self.board = [[0]*self.cols]*self.rows
		for row in xrange(self.rows):
			for col in xrange(self.cols):
				space = boardStr[row * self.cols + col]
				if space == ".":
					self.board[row][col] = None
				else:
					color = "B" if space.islower() else "W"
					newPiece = Piece(self, color, space.upper(), row, col)
					self.board[row][col] = newPiece
					if color == "B":
						self.blackSet.add(newPiece)
					else:
						self.whiteSet.add(newPiece)

	def getPieceAt(self, row, col):
		if row < 0 or row >= self.rows:
			return None
		if col < 0 or col >= self.cols:
			return None
		return self.board[row][col]

	def getWhitePieces(self):
		return self.whiteSet

	def getBlackPieces(self):
		return self.blackSet

	def getWhiteKing(self):
		for white in self.whiteSet:
			if white.type == "K":
				return white

	def getBlackKing(self):
		for black in self.blackSet:
			if black.type == "K":
				return black

class Piece:

	def __init__(self, board, color, type, row, col):
		self.board = board
		self.color = color
		self.type = type
		self.row = row
		self.col = col

	def getPosition(self):
		return (self.row, self.col)

	def getMoves(self):
		if self.type == "P": # Pawn
			moves = set()
		elif self.type == "R": # Rook
			moves = self._getStraightMoves()
		elif self.type == "N": # Knight
			moves = set()
			moves.add((self.row+2, self.col+1))
			moves.add((self.row+2, self.col-1))
			moves.add((self.row+1, self.col+2))
			moves.add((self.row+1, self.col-2))
			moves.add((self.row-1, self.col+2))
			moves.add((self.row-1, self.col-2))
			moves.add((self.row-2, self.col+1))
			moves.add((self.row-2, self.col-1))
		elif self.type == "B": # Bishop
			moves = self._getDiagonalMoves()
		elif self.type == "Q": # Queen
			moves = self._getDiagonalMoves() | self._getStraightMoves()
		elif self.type == "K": # King
			moves = set()
		return moves

	def _getStraightMoves(self):
		moves = set()
		# North
		for row in xrange(self.row+1, self.board.rows):
			moves.add((row, self.col))
			if self.board.getPieceAt(row, self.col):
				break
		# South
		for row in xrange(self.row-1, -1, -1):
			moves.add((row, self.col))
			if self.board.getPieceAt(row, self.col):
				break
		# East
		for col in xrange(self.col+1, self.board.cols):
			moves.add((self.row, col))
			if self.board.getPieceAt(self.row, col):
				break
		# West
		for col in xrange(self.col-1, -1, -1):
			moves.add((self.row, col))
			if self.board.getPieceAt(self.row, col):
				break
		return moves

	def _getDiagonalMoves(self):
		moves = set()
		#Northeast
		row = self.row+1
		col = self.col+1
		while row < self.board.rows and col < self.board.cols:
			moves.add((row, col))
			if self.board.getPieceAt(row, col):
				break
			row+=1
			col+=1
		#Southeast
		row = self.row-1
		col = self.col+1
		while row >= 0 and col < self.board.cols:
			moves.add((row, col))
			if self.board.getPieceAt(row, col):
				break
			row-=1
			col+=1
		#Northwest
		row = self.row+1
		col = self.col-1
		while row < self.board.rows and col >= 0:
			moves.add((row, col))
			if self.board.getPieceAt(row, col):
				break
			row+=1
			col-=1
		#Southwest
		row = self.row-1
		col = self.col-1
		while row >= 0 and col >= 0:
			moves.add((row, col))
			if self.board.getPieceAt(row, col):
				break
			row-=1
			col-=1
		return moves

def is_check(table):
	board = Board(table)
	whiteKing = board.getWhiteKing()
	blackKing = board.getBlackKing()
	for white in board.getWhitePieces():
		if blackKing.getPosition() in white.getMoves():
			print "Black"
			return
	for black in board.getBlackPieces():
		if whiteKing.getPosition() in black.getMoves():
			print "White"
			return
	print "None"

table = "..r.........k.......p.....p..........................nPP..B...RK" #White
is_check(table)
