books = ["After Many a Summer Dies the Swan"]
tweets = ["The birch canoe slid on the smooth planks ", "Glue the sheet to the dark blue background", "After Many a Summer Dies the Swan The birch canoe slid on the smooth planks ", "Glue the sheet to the dark blue background After Many a Summer Dies the Swan"]
w = 1

def extract_contexts(books, tweets, w):
	for tweet in tweets:
		for book in books:
			if book in tweet:
				context = tweet.replace(book, "-TITLE-")
				contextArray = context.split()
				index = contextArray.index("-TITLE-")
				start = max(index-w, 0)
				end = min(index+w+1, len(contextArray))
				print ' '.join(contextArray[start:end])
				break

extract_contexts(books, tweets, w)
