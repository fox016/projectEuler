class Program:

	def __init__(self):
		self.statements = []

	def addStatement(self, statment)
		self.statements.append(statement)

class Declaration:

	def __init__(self, variable, type):
		self.variable = variable
		self.type = type

class Assignment:

	def __init__(self, variable, expression):
		self.variable = variable
		self.expression = expression

class If:
	
	def __init__(self, if_expr, then_expr, else_expr=None):
		self.if_expr = if_expr
		self.then_expr = then_expr
		self.else_expr = else_expr

class While:

	def __init__(self, expr, statement):
		self.expr = expr
		self.statement = statement

class Block:

	def __init__(self):
		self.statements = []

	def addStatement(self, statement)
		self.statements.append(statement)

class Expression:

	def __init__(self, left_expr, op, right_expr):
		self.left_expr = left_expr
		self.op = op
		self.right_expr = right_expr

class Arithmetic:

	def __init__(self, left_factor, op, right_factor):
		self.left_factor = left_factor
		self.op = op
		self.right_factor = right_factor

class Constant:

	def __init__(self, value):
		self.value = value

class Variable:

	def __init__(self, name):
		self.name = name

def semantic(ast):
	print ast

ast = "PROGRAM\n    DECLARATION\n        VARIABLE\n            a\n        integer\n    IF\n        CONSTANT\n            1\n        ASSIGNMENT\n            VARIABLE\n                a\n            CONSTANT\n                2\n"
semantic(ast)
