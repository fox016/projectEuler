import re
import urllib3

pool = urllib3.PoolManager()
headers = {"Cookie": "BIGipServerwww.myfamily.com=658574346.20480.0000; ua=1; BIT=w4hzQYXdfj3ocMlxu3dWMkcZ_8G4Sa2TminEKEVLziI; SIT=1e6nlglASup4E0_LZbv82oRHpHB-i8-R8eWaMXuzOKG; AZT=mgtw0mdXMyKBI9K0d8351n-AwADMwAzUVNVRS5ekpBg; SI=jO3RFhHkfhTItHHHC3IUBm-AuHZaAI*V6D*DoP*DkS4SqAI3ROQ7UlQTVkRQR1OvcXauRXZyBA; EAZT=2z1C5rdtRA7MaddvqLvPEm-ABhVRTB; MFLANDING=1; tz=360; BIGipServerwww.myfamily.com-v1=708905994.0.0000; TZ=360; VTX=1; ATT=vRs2Z-WmXjJeJe8ehRglzE*CvPAxWSHADxmGAU; _ref=content%2Fview%2FNEWS; MF10=true; s_cc=true; s_sq=myfamily2%3D%2526pid%253D//www.myfamily.com/Choose%2526pidt%253D1%2526oid%253Dhttp%25253A//www.myfamily.com/isapi.dll%25253Fc%25253Dsite%252526htx%25253Dmain%2526ot%253DA"}

scriptRegex = re.compile("<script(.*?)</script(.*?)>", flags=re.IGNORECASE|re.DOTALL)
styleRegex = re.compile("<style(.*?)</style(.*?)>", flags=re.IGNORECASE|re.DOTALL)
tagRegex = re.compile(r'<.*?>')

linkFile = open("links.txt", "r")
newsFile = open("my_family_news.txt", "w") # Start new data file

for link in linkFile:
	url = "http://www.myfamily.com" + link
	req = pool.request("GET", url, None, headers)
	page = req.data
	page = page[page.find('<table border="0" cellspacing="0" cellpadding="0" class=BodyBG>'):page.find('<font color="ffffff">About Us</font>')]
	page = scriptRegex.sub("", page)
	page = styleRegex.sub("", page)
	page = page.replace("<br>", "\n")
	page = page.replace("<p>", "\n")
	page = tagRegex.sub("", page)
	page = page.replace("&nbsp;", " ")
	page = page.replace("&quot;", "\"")
	newsFile.write(page)
linkFile.close()
newsFile.close()
