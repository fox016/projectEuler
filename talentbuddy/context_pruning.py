
def context_pruning(contexts, triggers):
	for context in contexts:
		words = context.split()
		trigger = get_highest_trigger(words, triggers)
		if trigger == "":
			continue
		center = words.index("-TITLE-")
		tokenLoc = words.index(trigger)
		if tokenLoc < center:
			output = words[tokenLoc:min(center+2,len(words))]
		else:
			output = words[max(center-1,0):tokenLoc+1]
		print ' '.join(output)

def get_highest_trigger(words, triggers):
        index = max(map(lambda c: triggers.index(c) if (c in triggers) else -1, words))
	if index == -1:
		return ""
	return triggers[index]

contexts = ["-TITLE- The birch canoe", "dark blue background -TITLE- ", "juice -TITLE- of lemons makes", "of steady work -TITLE- faced us", "A -TITLE- large size in", "there when the -TITLE- sun rose", "flame and heat -TITLE- ", "The salt breeze -TITLE- came across from", "fish -TITLE- twisted and turned", "the pants and -TITLE- sew a button"]
triggers = ["when", "button", "canoe", "dark", "sew"]

context_pruning(contexts, triggers)
