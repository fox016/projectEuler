def extract_books(contexts, tweets):
	titles = set()
	for tweet in tweets:
		for context in contexts:
			sides = context.split("-TITLE-")
			start, end = 0, 0
			if sides[0] == " ":
				start = 0
			elif sides[0] in tweet:
				start = tweet.index(sides[0]) + len(sides[0])
			else:
				continue
			if sides[1] == " ":
				end = len(tweet)
			elif sides[1] in tweet:
				end = tweet.index(sides[1])
			else:
				continue
			if start > end:
				continue
			titles.add(tweet[start:end])
			break
	titles.discard("")
	for title in sorted(titles):
		print title

contexts = ["on the smooth -TITLE- planks", "sheet -TITLE- to the dark", "It's -TITLE- easy to tell the", "leg -TITLE- is a", " -TITLE- is", "of -TITLE- lemons", " -TITLE- thrown", "chopped corn -TITLE- and", "work faced us -TITLE- ", "A -TITLE- large size"]
tweets = ["The birch canoe slid on the smooth planks", "The birch canoe slid on the smooth After Many a Summer Dies the Swan planks", "Glue the sheet to the dark blue background", "Glue the sheet Ah, Wilderness! to the dark blue background", "It's easy to tell the depth of a well", "It's All Passion Spent easy to tell the depth of a well", "These days a chicken leg is a rare dish", "These days a chicken leg All the King's Men is a rare dish", "Rice is often served in round bowls", "Rice Alone on a Wide, Wide Sea is often served in round bowls", "The juice of lemons makes fine punch", "The juice of An Acceptable Time lemons makes fine punch", "The box was thrown beside the parked truck", "The box was Antic Hay thrown beside the parked truck", "The hogs were fed chopped corn and garbage", "The hogs were fed chopped corn An Evil Cradling and garbage", "Four hours of steady work faced us", "Four hours of steady work faced us Arms and the Man", "A large size in stockings is hard to sell", "A As I Lay Dying large size in stockings is hard to sell", "The boy was there when the sun rose", "A rod is used to catch pink salmon", "The source of the huge river is the clear spring", "Kick the ball straight and follow through", "Help the woman get back to her feet", "A pot of tea helps to pass the evening", "Smoky fires lack flame and heat", "The soft cushion broke the man's fall", "The salt breeze came across from the sea", "The girl at the booth sold fifty bonds", "The small pup gnawed a hole in the sock", "The fish twisted and turned on the bent hook", "Press the pants and sew a button on the vest", "The swan dive was far short of perfect", "The beauty of the view stunned the young boy", "Two blue fish swam in the tank", "Her purse was full of useless trash", "The colt reared and threw the tall rider", "It snowed, rained, and hailed the same morning", "Read verse out loud for pleasure", "Hoist the load to your left shoulder", "Take the winding path to reach the lake", "Note closely the size of the gas tank", "Wipe the grease off his dirty face", "Mend the coat before you go out", "The wrist was badly strained and hung limp", "The stray cat gave birth to kittens", "The young girl gave no clear response", "The meal was cooked before the bell rang", "What joy there is in living", "A king ruled the state in the early days", "The ship was torn apart on the sharp reef", "Sickness kept him home the third week", "The wide road shimmered in the hot sun", "The lazy cow lay in the cool grass", "Lift the square stone over the fence", "The rope will bind the seven books at once", "Hop over the fence and plunge in", "The friendly gang left the drug store", "Mesh wire keeps chicks inside", "The frosty air passed through the coat", "The crooked maze failed to fool the mouse", "Adding fast leads to wrong sums", "The show was a flop from the very start", "A saw is a tool used for making boards", "The wagon moved on well oiled wheels", "March the soldiers past the next hill", "A cup of sugar makes sweet fudge", "Place a rosebush near the porch steps", "Both lost their lives in the raging storm", "We talked of the side show in the circus", "Use a pencil to write the first draft", "He ran half way to the hardware store", "The clock struck to mark the third period", "A small creek cut across the field", "Cars and busses stalled in snow drifts", "The set of china hit the floor with a crash", "This is a grand season for hikes on the road", "The dune rose from the edge of the water", "Those words were the cue for the actor to leave", "A yacht slid around the point into the bay", "The two met while playing on the sand", "The ink stain dried on the finished page", "The walled town was seized without a fight", "The lease ran out in sixteen weeks", "A tame squirrel makes a nice pet", "The horn of the car woke the sleeping cop", "The heart beat strongly and with firm strokes", "The pearl was worn in a thin silver ring", "The fruit peel was cut in thick slices", "The Navy attacked the big task force", "See the cat glaring at the scared mouse", "There are more than two factors here", "The hat brim was wide and too droopy", "The lawyer tried to lose his case", "The grass curled around the fence post", "Cut the pie into large parts", "Men strive but seldom get rich", "Always close the barn door tight", "He lay prone and hardly moved a limb", "The slush lay deep along the street", "A wisp of cloud hung in the blue air", "A pound of sugar costs more than eggs", "The fin was sharp and cut the clear water", "The play seems dull and quite stupid", "Bail the boat to stop it from sinking", "The term ended in late june that year", "A Tusk is used to make costly gifts", "Ten pins were set in order", "The bill was paid every third week"]

extract_books(contexts, tweets)
