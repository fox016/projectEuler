def decrypt(message, key):
	keyIndex = 0
	while len(message) > len(key):
		key.append(key[keyIndex])
		keyIndex += 1
		keyIndex %= 3
	plain = map(lambda m, k: ord(m) ^ k, list(message), key)
	return ''.join(map(chr, plain))

enc = ''.join(map(chr, [map(int, lines.split(',')) for lines in open('files/59.dat', 'r')][0]))
for k1 in xrange(97, 123):
	for k2 in xrange(97, 123):
		for k3 in xrange(97, 123):
			plain = decrypt(enc, [k1, k2, k3])
			if " the " in plain:
				print plain
				print map(chr, [k1, k2, k3])
				print sum(map(ord, list(plain)))
				exit(0)
