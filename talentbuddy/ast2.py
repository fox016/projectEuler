def ast(source):
	source = source.replace(" ", "")
	parseProgram(source, 0)

def parseProgram(program, level):
	print ("    " * level) + "PROGRAM"
	parseStatementList(program, level)

def parseStatementList(statementList, level):
	semicolons = []
	state = 0
	for i in xrange(len(statementList)):
		if statementList[i] == "{":
			state += 1
		elif statementList[i] == "}":
			state -= 1
		elif statementList[i] == ";":
			if state == 0:
				semicolons.append(i)
	start = 0
	for i in semicolons:
		parseStatement(statementList[start:i], level+1)
		start = i+1
	parseStatement(statementList[start:], level+1)

def parseStatement(statement, level):
	if statement.startswith("integer") or statement.startswith("boolean"):
		parseDeclaration(statement, level)
	elif statement.startswith("if"):
		parseIf(statement, level)
	elif statement.startswith("while"):
		parseWhile(statement, level)
	elif statement.startswith("{"):
		print ("    " * level) + "BLOCK"
		parseStatementList(statement[1:-1], level)
	else:
		parseAssignment(statement, level)

def parseDeclaration(dec, level):
	print ("    " * level) + "DECLARATION"
	type = dec[0:7]
	var = dec[7:]
	parseVariable(var, level+1)
	print ("    " * (level+1)) + type

def parseIf(ifState, level):
	print ("    " * level) + "IF"
	index = ifState.index("then")
	expr = ifState[2:index]
	parseExpression(expr, level+1)
	statement = ifState[index+4:]
	if "else" not in statement:
		parseStatement(statement, level+1)
	else:
		index = statement.index("else")
		parseStatement(statement[0:index], level+1)
		parseStatement(statement[index+4:], level+1)

def parseWhile(whileState, level):
	print ("    " * level) + "WHILE"
	index = whileState.index("do")
	expr = whileState[5:index]
	parseExpression(expr, level+1)
	statement = whileState[index+2:]
	parseStatement(statement, level+1)

def parseAssignment(assignment, level):
	print ("    " * level) + "ASSIGNMENT"
	index = assignment.index("=")
	parseVariable(assignment[0:index], level+1)
	parseExpression(assignment[index+1:], level+1)

def parseVariable(variable, level):
	print ("    " * level) + "VARIABLE"
	print ("    " * (level+1)) + variable

def parseExpression(expr, level):
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
		parseFactor(math[0:index], level+1)
		print ("    " * (level+1)) + "+"
		parseFactor(math[index+1:], level+1)
	elif "-" in math:
		print ("    " * level) + "ARITHMETIC"
		index = math.index("-")
		parseFactor(math[0:index], level+1)
		print ("    " * (level+1)) + "-"
		parseFactor(math[index+1:], level+1)
	else:
		parseFactor(math, level)

def parseFactor(factor, level):
	if factor in ["true", "false"] or isNumber(factor):
		parseConstant(factor, level)
	else:
		parseVariable(factor, level)

def parseConstant(constant, level):
	print ("    " * level) + "CONSTANT"
	print ("    " * (level+1)) + constant

def isNumber(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

source = "integer a; integer b; if true then { a = 3; b = 7 }; while b > 0 do b = b - a; if b == 0 then b = a else b = 5"
ast(source)
