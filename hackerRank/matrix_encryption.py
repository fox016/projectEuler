import math

def get_dimensions(n):
	sqrt = n**0.5
	width = int(math.floor(sqrt))
	height = 1
	while height <= int(math.ceil(sqrt)):
		if height > width:
			width+=1
			height = 1
		elif width * height >= n:
			return (width, height)
		else:
			height+=1

def pad_message(message, length):
	while len(message) < length:
		message += "*"
	return message

message = raw_input()
width, height = get_dimensions(len(message))
message = pad_message(message, width * height)
words = []
for start in xrange(width):
	word = ""
	for index in xrange(start, len(message), width):
		word += message[index]
	words.append(word.replace("*", ""))
print ' '.join(words)
