for test in xrange(int(raw_input())):
	s = raw_input()
	begin_index = 0
	end_index = len(s)-1
	while begin_index < end_index:
		if s[begin_index] == s[end_index]:
			begin_index+=1
			end_index-=1
		else:
			if s[begin_index+1] == s[end_index]:
				begin_index = begin_index
			else:
				begin_index = end_index 
			break
	print begin_index
