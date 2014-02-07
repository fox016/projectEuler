rounds = [line.split() for line in open("files/54.dat", 'r')]

values = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

def isFlush(hand):
	for card in hand:
		if hand[0][1] != card[1]:
			return False
	return True

def isStraight(hand):
	for i in xrange(len(hand)-1):
		if values[hand[i][0]]+1 != values[hand[i+1][0]]:
			return False
	return True

def hasSet(hand, size):
	for i in xrange(len(hand)-(size-1)):
		hasSet = True
		for j in xrange(1, size):
			hasSet = hasSet and hand[i][0] == hand[i+j][0]
			if not hasSet: break
		if not hasSet: continue
		return True
	return False

def isFullHouse(hand):
	if hand[0][0] == hand[1][0] and hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0]:
		return True
	if hand[0][0] == hand[1][0] and hand[2][0] == hand[3][0] and hand[3][0] == hand[4][0]:
		return True
	return False

def hasTwoPair(hand):
	if hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0]:
		return True
	if hand[0][0] == hand[1][0] and hand[3][0] == hand[4][0]:
		return True
	if hand[0][0] == hand[1][0] and hand[2][0] == hand[3][0]:
		return True
	return False

def getTieWinner(hand1, hand2):
	for i in xrange(len(hand1)-1, -1, -1):
		if values[hand1[i][0]] < values[hand2[i][0]]:
			return 2
		if values[hand1[i][0]] > values[hand2[i][0]]:
			return 1

def getSetWinner(hand, size):
	for i in xrange(len(hand)-(size-1)):
		hasSet = True
		for j in xrange(1, size):
			hasSet = hasSet and hand[i][0] == hand[i+j][0]
			if not hasSet: break
		if not hasSet: continue
		return values[hand[i][0]]

def getFullHouseWinner(hand):
	if hand[0][0] == hand[1][0] and hand[1][0] == hand[2][0] and hand[3][0] == hand[4][0]:
		return values[hand[0][0]]
	return values[hand[4][0]]

def getTwoPairWinner(hand):
	if hand[0][0] == hand[1][0] and hand[2][0] == hand[3][0]:
		return values[hand[3][0]]
	return values[hand[4][0]]
		
def getHighestWinner(hand):
	if isFlush(hand) or isStraight(hand):
		return values[hand[4][0]]
	if isFullHouse(hand):
		return getFullHouseWinner(hand);
	if hasTwoPair(hand):
		return getTwoPairWinner(hand);
	if hasSet(hand, 4):
		return getSetWinner(hand, 4);
	if hasSet(hand, 3):
		return getSetWinner(hand, 3);
	if hasSet(hand, 2):
		return getSetWinner(hand, 2);
	return values[hand[4][0]]

def getRank(hand):
	if isFlush(hand):
		if isStraight(hand):
			if hand[0][0] == "T":
				return 10
			return 9
		return 6
	if hasSet(hand, 4):
		return 8
	if isFullHouse(hand):
		return 7
	if isStraight(hand):
		return 5
	if hasSet(hand, 3):
		return 4
	if hasTwoPair(hand):
		return 3
	if hasSet(hand, 2):
		return 2
	return 1

def isPlayerOne(hand1, hand2):
	if getRank(hand1) > getRank(hand2):
		return True
	elif getRank(hand1) == getRank(hand2):
		if getHighestWinner(hand1) > getHighestWinner(hand2):
			return True
		if getHighestWinner(hand1) < getHighestWinner(hand2):
			return False
		return getTieWinner(hand1, hand2) == 1
	return False

oneWins = 0
for round in rounds:
	hand1 = sorted(round[0:5], key=lambda card: values[card[0]])
	hand2 = sorted(round[5:], key=lambda card: values[card[0]])
	if isPlayerOne(hand1, hand2):
		oneWins += 1
print oneWins
