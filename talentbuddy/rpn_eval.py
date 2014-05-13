ops = {
	"+": lambda x, y: int(y) + int(x),
	"-": lambda x, y: int(y) - int(x),
	"*": lambda x, y: int(y) * int(x),
	"/": lambda x, y: int(y) / int(x),
} 

def rpn_eval(expr):
	stack = []
	num = ""
	for i in xrange(len(expr)):
		if expr[i] in " +-*/~":
			if num != "":
				stack.append(num)
				num = ""
		if expr[i] in "+-*/~":
			if expr[i] == "~":
				stack.append(int(stack.pop()) * -1)
			else:
				stack.append(ops[expr[i]](stack.pop(), stack.pop()))
		elif is_number(expr[i]):
			num += expr[i]
	print stack.pop()

def is_number(s):
	try:
		float(s)
		return True
	except ValueError:
		return False

expr = "101 303 + 2/1~%%%1-+"
rpn_eval(expr)
