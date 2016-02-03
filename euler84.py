import random

squares = [
	"GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3",
	"JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3",
	"FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3",
	"G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2"
]
dice = range(1, 5)
position = 0
rolls = 1000000
square_count_map = {}
for square in squares:
	square_count_map[square] = 0
doubles_count = 0

def draw_cc(position, square):
	card_num = random.randint(0, 15)
	if(card_num == 0):
		return 0, "GO"
	if(card_num == 1):
		return 10, "JAIL"
	return position, square

def draw_ch(position, square):
	card_num = random.randint(0, 15)
	if(card_num == 0):
		return 0, "GO"
	if(card_num == 1):
		return 10, "JAIL"
	if(card_num == 2):
		return 11, "C1"
	if(card_num == 3):
		return 24, "E3"
	if(card_num == 4):
		return 39, "H2"
	if(card_num == 5):
		return 5, "R1"
	if(card_num == 6 or card_num == 7):
		if position < 5:
			return 5, "R1"
		if position < 15:
			return 15, "R2"
		if position < 25:
			return 25, "R3"
		if position < 35:
			return 35, "R4"
		return 5, "R1"
	if(card_num == 8):
		if position < 12:
			return 12, "U1"
		if position < 28:
			return 28, "U2"
		return 12, "U1"
	if(card_num == 9):
		if position == 7:
			return 4, "T1"
		if position == 22:
			return 19, "D3"
		if position == 36:
			return draw_cc(33, "CC3")
	return position, square

for i in xrange(rolls):
	d1 = random.choice(dice)
	d2 = random.choice(dice)
	if(d1 == d2):
		doubles_count += 1
	else:
		doubles_count = 0
	if(doubles_count == 3):
		square = "JAIL"
		position = 10
		doubles_count = 0
	else:
		position += (d1 + d2)
		position %= len(squares)
		square = squares[position]
	if(square == "G2J"):
		square = "JAIL"
		position = 10
	elif(square[:2] == "CC"):
		position, square = draw_cc(position, square)
	elif(square[:2] == "CH"):
		position, square = draw_ch(position, square)
	square_count_map[square]+=1

for square in squares:
	print square, square_count_map[square], round(square_count_map[square] / float(rolls), 4)
