def arithmetic_eval(expr):
	expr = expr.replace(" ", "")
	expr = expr.replace("-", "~")
	print my_eval(expr)

def my_eval(expr):
	for i in xrange(len(expr)):
		if expr[i] == "(":
			endPos = get_end_paren(expr, i)
			first = expr[0:i]
			middle = expr[i+1:endPos]
			last = ""
			if endPos+1 < len(expr):
				last = expr[endPos+1:]
			return my_eval(first + str(my_eval(middle)) + last)
	for i in xrange(len(expr)-1, -1, -1):
		if expr[i] in ["+", "~"]:
			return interp(expr[i], expr[0:i], expr[i+1:])
	for i in xrange(len(expr)-1, -1, -1):
		if expr[i] == "*":
			return interp(expr[i], expr[0:i], expr[i+1:])
	return int(expr)

def interp(op, lhs, rhs):
	if op == "+":
		return my_eval(lhs) + my_eval(rhs)
	if op == "~":
		return my_eval(lhs) - my_eval(rhs)
	if op == "*":
		return my_eval(lhs) * my_eval(rhs)

def get_end_paren(expr, startPos):
	state = 1
	for i in xrange(startPos+1, len(expr)):
		if expr[i] == "(":
			state += 1
		if expr[i] == ")":
			state -= 1
			if state == 0:
				return i
	return None

expr = "4 * (2 + 3 * (9 - 7))"
arithmetic_eval(expr)
