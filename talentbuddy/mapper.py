mod = 104677
mod_exp_table = []

def get_hash(message):
	
	global mod
	global mod_exp_table

	hash = 0
	m = len(message)
	for i in xrange(1, m+1):
		hash += (ord(message[i-1]) * mod_exp_table[m-i])
		hash = hash % mod
	return hash

def has_match(value, value_hash, doc):

	global mod
	global mod_exp_table

        hash = get_hash(doc[0:len(value)])
        if hash == value_hash:
		return True
        for prev_index in xrange(len(doc) - len(value)):
                hash = ((hash - (ord(doc[prev_index]) * mod_exp_table[len(value)-1])) * 10 + ord(doc[prev_index+len(value)])) % mod
                if hash == value_hash:
			if value[0] == doc[prev_index+1]:
				return True
	return False

def mr_map(search_strings, docs):

	global mod
	global mod_exp_table
	mod_exp_table = [pow(10, m, mod) for m in xrange(200000)]

	search_hashes = map(get_hash, search_strings)

	for searchIndex in xrange(len(search_strings)):
		indexList = []
		for docIndex in xrange(len(docs)):
			if has_match(search_strings[searchIndex], search_hashes[searchIndex], docs[docIndex]):
				indexList.append(docIndex)
		if not indexList:
			print -1
		else:
			print ' '.join(map(str, indexList))

searchStrings = ["cr", "fv", "ur", "az", "qx", "ja", "nh"]
docs = ["hpqbjanfvxcrenhpuoqjpeztburqxszcetvxazduony", "xfvwtojhqnoscbmprswiyape", "dinwdurcxetjadazyertokofvqxpcrnnhux", "furcxpmcrkpwgiivqfvaznhcovyaqxjahyfkvtgjyy", "lhfzzdysfxfrkrsxxtdxcfpqb", "vfvfaotazwiggmjaqxwaurlanfgmcrtnhdb"]
mr_map(searchStrings, docs)
