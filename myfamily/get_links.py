import re
import urllib3

maxrows = 99
offset = 0
pool = urllib3.PoolManager()
headers = {"Cookie": "BIGipServerwww.myfamily.com=658574346.20480.0000; ua=1; BIT=w4hzQYXdfj3ocMlxu3dWMkcZ_8G4Sa2TminEKEVLziI; SIT=1e6nlglASup4E0_LZbv82oRHpHB-i8-R8eWaMXuzOKG; AZT=mgtw0mdXMyKBI9K0d8351n-AwADMwAzUVNVRS5ekpBg; SI=jO3RFhHkfhTItHHHC3IUBm-AuHZaAI*V6D*DoP*DkS4SqAI3ROQ7UlQTVkRQR1OvcXauRXZyBA; EAZT=2z1C5rdtRA7MaddvqLvPEm-ABhVRTB; MFLANDING=1; tz=360; BIGipServerwww.myfamily.com-v1=708905994.0.0000; TZ=360; VTX=1; ATT=vRs2Z-WmXjJeJe8ehRglzE*CvPAxWSHADxmGAU; _ref=content%2Fview%2FNEWS; MF10=true; s_cc=true; s_sq=myfamily2%3D%2526pid%253D//www.myfamily.com/Choose%2526pidt%253D1%2526oid%253Dhttp%25253A//www.myfamily.com/isapi.dll%25253Fc%25253Dsite%252526htx%25253Dmain%2526ot%253DA"}

linkRegex = re.compile("<a href=(\"|')(.*?)(\"|')", flags=re.DOTALL)

fo = open("links.txt", "w") # Start new data file
links = set([])

while offset < 35940:
	url = "http://www.myfamily.com/isapi.dll?c=Content&htx=List&siteid=uHZaAI&contentclass=NEWS&categoryid=0&search=&maxrows=" + str(maxrows) + "&offset=" + str(offset)
	offset += maxrows
	req = pool.request("GET", url, None, headers)
	status = req.status
	page = req.data

	if status != 200:
		print "Error", status, page
		raise SystemExit(0)

	match = linkRegex.search(page)
	while match:
		link = match.group(2)
		contentid = link[link.find("contentid="):]
		contentid = contentid[0:18]
		link = link[0:link.find("contentid=")] + contentid + "&contentclass=NEWS"
		match = linkRegex.search(match.string[match.end():])
		if link.startswith("/isapi.dll?c=content") and link not in links:
			links.add(link)
			fo.write(link + "\n")
