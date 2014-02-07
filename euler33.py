product = 1.0
for num in xrange(10, 100):
	for den in xrange(num+1, 100):
		if den % 10 == 0:
			continue
		if str(num)[0] == str(den)[0]:
			if float(str(num)[1]) / float(str(den)[1]) == float(num) / float(den):
				product *= float(num) / float(den)
		elif str(num)[0] == str(den)[1]:
			if float(str(num)[1]) / float(str(den)[0]) == float(num) / float(den):
				product *= float(num) / float(den)
		elif str(num)[1] == str(den)[0]:
			if float(str(num)[0]) / float(str(den)[1]) == float(num) / float(den):
				product *= float(num) / float(den)
		elif str(num)[1] == str(den)[1]:
			if float(str(num)[0]) / float(str(den)[0]) == float(num) / float(den):
				product *= float(num) / float(den)
print product
