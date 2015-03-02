
def guess_combo(locks, combo_len, turn_amount):
	combo = ""
	for i in xrange(combo_len):
		combo_probs = [0] * 10
		for lock in locks:
			digit = int(lock[i])
			combo_probs[digit] += 1
			for turn in xrange(1,turn_amount+1):
				combo_probs[(digit-turn)%10] += 1
				combo_probs[(digit+turn)%10] += 1
		combo += str(get_max_index(combo_probs))
		print combo_probs
	print combo

def get_max_index(num_list):
	best = (0, 0)
	for i in xrange(len(num_list)):
		if num_list[i] > best[0]:
			best = (num_list[i], i)	
	return best[1]

locks = ["0052", "3333", "2222", "3225", "9444", "3336", "9414"]
combo_len = 4
turn_amount = 3
guess_combo(locks, combo_len, turn_amount)
