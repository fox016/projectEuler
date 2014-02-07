logins = [int(line) for line in open('files/79.dat', 'r')]

digits = set(list("".join([str(log) for log in logins])))

after = {}
for d in digits:
	after[d] = set()

for log in logins:
	for i in xrange(3):
		for a in xrange(i+1, 3):
			after[str(log)[i]].add(str(log)[a])

print "".join(sorted(after, key = lambda a: len(after[a]), reverse=True))
