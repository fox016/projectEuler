ROUNDS = 15

def calc_denomenator_odds():
	return reduce(lambda x,y: x*y, [i+2 for i in xrange(ROUNDS)], 1)

def more_true(game):
	true_count = game.count(True)
	return true_count > (len(game) - true_count)

def calc_numerator_odds(game):
	if not more_true(game):
		return 0
	total = 1
	for i in xrange(ROUNDS):
		if not game[i]:
			total *= (i+1)
	return total

def calc_total_numerator():
	total = 0
	game = [True] * ROUNDS
	while True:
		total += calc_numerator_odds(game)
		pos = ROUNDS - 1
		while pos >= 0 and not game[pos]:
			game[pos] = True
			pos-=1
		if pos == -1:
			break
		game[pos] = False
	return total

print calc_denomenator_odds() / calc_total_numerator()
