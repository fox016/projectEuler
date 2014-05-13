def reveal_image(input, sample, cols, rows, score):
	input = list(input)
	sample = map(ord, sample)
	mean = float(sum(sample)) / len(sample)
	dev = float(score) * std_dev(sample, mean)
	for row in xrange(rows):
		for col in xrange(cols):
			current = ord(input[row * cols + col])
			if current >= (mean - dev) and current <= (mean + dev):
				input[row * cols + col] = "X"
			else:
				input[row * cols + col] = "."
		print ''.join(input[row*cols:(row+1)*cols])

def std_dev(nums, mean):
	return ((1.0 / len(nums)) * (sum(map(lambda n: (n - mean)**2.0, nums))))**0.5

input = ",7.G?DBIA!i870*MNm]1mpzLxIGJFC:F>-`O&^FEHD@:H;H)w||KIHB)yhY]BKB?>C9GKJCZiF;K<K>FDKAB;=HBDGKEIKD:IAI>=J?KAB>n8B:C:A=HCB:FS)DJKI=?D4gK:>::@A>C9?G$LB?BGK?FBGP^o.]<;?IA46QR1BBA>JJCC<<2+GIA@@I:B;!td-MA>CG?7*gM];JGKKKAHB8r#zFAB>KKJI2p0S>9KII:@X`6+FB><KH<Jb7$h58`|GF?H:Yz@IBIFDA@E99]uK?JOvN.*xSd(-NYSN!d<;G@G:E:A9>9IF??H=GMcnz7X_oa1kw5x%hZ<dx8uSQnk1gvYl)j+KJ|tia$|T]z&dOO*SkYU<<6(7a.`!QQ)]j0K>rx}3vl0_wXNfNno_jar*nB@h-kR!0oVS?D5UZ#T)b1ft]hZg{3vetg%8&5H>>K<:A9:;>$gRd$`ie1z{+mdVap-vqQg2rP*v$?K>KH^vzg%bkQ*Vdo!e+7"
sample = "<?BEH"
cols = 36
rows = 14
score = "2.15"
reveal_image(input, sample, cols, rows, score)
