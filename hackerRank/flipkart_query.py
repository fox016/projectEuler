keywords = {
	"axe": ("axe deo", 1),
	"deo": ("axe deo", 1),
	"deodorant": ("axe deo", 2),
	"combo": ("axe deo", 4),
	"combos": ("axe deo", 4),
	"best": ("best-seller books", 1),
	"best-seller": ("best-seller books", 1),
	"book": ("best-seller books", 3),
	"books": ("best-seller books", 2),
	"calvin": ("calvin klein", 1),
	"klein": ("calvin klein", 1),
	"camcorder": ("camcorder", 1),
	"camcorders": ("camcorder", 1),
	"video": ("camcorder", 1),
	"camera": ("camera", 2),
	"cameras": ("camera", 2),
	"chemistry": ("chemistry", 1),
	"science": ("chemistry", 2),
	"chrome": ("chromebook", 1),
	"google": ("chromebook", 1),
	"chromebook": ("chromebook", 1),
	"chromebooks": ("chromebook", 1),
	"c": ("c programming", 1),
	"programming": ("c programming", 1),
	"data": ("data structures algorithms", 1),
	"structures": ("data structures algorithms", 1),
	"structure": ("data structures algorithms", 1),
	"algorithms": ("data structures algorithms", 1),
	"algorithm": ("data structures algorithms", 1),
	"dell": ("dell laptops", 1),
	"laptop": ("dell laptops", 1),
	"laptops": ("dell laptops", 1),
	"dslr": ("dslr canon", 1),
	"slr": ("dslr canon", 1),
	"canon": ("dslr canon", 1),
	"mathematics": ("mathematics", 2),
	"math": ("mathematics", 2),
	"mathematician": ("mathematics", 1),
	"mathematicians": ("mathematics", 1),
	"nike": ("nike-deodrant", 1),
	"deodrant": ("nike-deodrant", 1),
	"nike-deodrant": ("nike-deodrant", 1),
	"nike-deodorant": ("nike-deodrant", 1),
	"nike-deodorant": ("nike-deodrant", 1),
	"physics": ("physics", 1),
	"physicist": ("physics", 1),
	"physicists": ("physics", 1),
	"sony": ("sony cybershot", 2),
	"cybershot": ("sony cybershot", 1),
	"audio": ("spoken english", 1),
	"spoken": ("spoken english", 1),
	"timex": ("timex watch", 1),
	"watch": ("timex watch", 2),
	"titan": ("titan watch", 1),
	"tommy": ("tommy watch", 1),
	"paperback": ("written english", 3),
}
illegal_chars = ["(", ")", ":", "?"]
products = []
for n in xrange(int(raw_input())):
	products.append(raw_input())
for product in products:
	for char in illegal_chars:
		product = product.replace(char, "")
	product = product.lower()
	queries = set()
	for word in product.split(" "):	
		if word in keywords:
			queries.add(keywords[word])
	if queries:
		print sorted(queries, key = lambda q: q[1])[0][0]
	else:
		print "written english"
