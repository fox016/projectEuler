def count_substr(s, t):
	total = 0
	i = 0
	while i <= len(t) - len(s):
		if t[i:i+len(s)] == s:
			total += 1
			i += len(s)
		else:
			i += 1
	print total

s = "aa"
t = "aaabaaaaa"
count_substr(s, t)

def count_tokens(a, t):
	tokens = list()
	inToken = False
	tokenStart = -1
	for i in xrange(len(t)):
		if t[i] in a and not inToken:
			inToken = True
			tokenStart = i
		if t[i] not in a and inToken:
			inToken = False
			tokens.append(t[tokenStart:i])
	if inToken:
		tokens.append(t[tokenStart:])
	print len(tokens)

a = "abc"
t = "abcdefabcdefaazbbazc"
count_tokens(a, t)
