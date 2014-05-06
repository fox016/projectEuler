def ast(source):
	source = source.replace(" ", "")
	parseProgram(source, 0)

def parseProgram(program, level):
	print ("    " * level) + "PROGRAM"
	for statement in program.split(";"):
		parseStatement(statement, level+1)

def parseStatement(statement, level):
	parseAssignment(statement, level)

def parseAssignment(assignment, level):
	print ("    " * level) + "ASSIGNMENT"
	index = assignment.index("=")
	parseVariable(assignment[0:index], level+1)
	parseExpression(assignment[index+1:], level+1)

def parseVariable(variable, level):
	print ("    " * level) + "VARIABLE"
	print ("    " * (level+1)) + variable

def parseExpression(expr, level):
	if expr in ["true", "false"] or isNumber(expr):
		parseConstant(expr, level)
		return
	if ">" in expr:
		print ("    " * level) + "EXPRESSION"
		index = expr.index(">")
		parseArithmetic(expr[0:index], level+1)
		print ("    " * (level+1)) + ">"
		parseArithmetic(expr[index+1:], level+1)
	elif "<" in expr:
		print ("    " * level) + "EXPRESSION"
		index = expr.index("<")
		parseArithmetic(expr[0:index], level+1)
		print ("    " * (level+1)) + "<"
		parseArithmetic(expr[index+1:], level+1)
	elif "==" in expr:
		print ("    " * level) + "EXPRESSION"
		index = expr.index("==")
		parseArithmetic(expr[0:index], level+1)
		print ("    " * (level+1)) + "=="
		parseArithmetic(expr[index+2:], level+1)
	else:
		parseArithmetic(expr, level)

def parseArithmetic(math, level):
	if "+" in math:
		print ("    " * level) + "ARITHMETIC"
		index = math.index("+")
		parseFactor(math[0:index], level)
		print ("    " * (level+1)) + "+"
		parseFactor(math[index+1:], level)
	elif "-" in math:
		print ("    " * level) + "ARITHMETIC"
		index = math.index("-")
		parseFactor(math[0:index], level)
		print ("    " * (level+1)) + "-"
		parseFactor(math[index+1:], level)
	else:
		parseFactor(math, level-1)

def parseFactor(factor, level):
	if factor in ["true", "false"] or isNumber(factor):
		parseConstant(factor, level+1)
	else:
		parseVariable(factor, level+1)

def parseConstant(constant, level):
	print ("    " * level) + "CONSTANT"
	print ("    " * (level+1)) + constant

def isNumber(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

source = "a = a - 1; b = b < b; c = c + c"
ast(source)
