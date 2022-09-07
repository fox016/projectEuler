# Download images from my wife's blogger account
import requests
import shutil
import re
from datetime import date
from datetime import timedelta

headers={'Cookie': 'TODO'} # get cookie value from chrome dev tools network request header

def get_img_links(html):
    links = []
    img_regex = "<img.*?>"
    src_regex = 'src="http([^"]+)"'
    img_match = re.search(img_regex, html)
    while img_match:
        img_tag = img_match.group(0)
        src_match = re.search(src_regex, img_tag)
        if src_match != None:
            links.append(src_match.group(1))
        img_match = re.search(img_regex, img_match.string[img_match.end():])
    return links

def download(link, filename):
    global headers
    response = requests.get(link, headers=headers, stream=True)
    with open("./bloggerImages/" + filename, "wb") as new_file:
        #response.raw.decode_content = True
        shutil.copyfileobj(response.raw, new_file)

def pad_left(text, char, length):
    while(len(text) < length):
        text = char + text
    return text

def run():
    day = date.today() - timedelta(days = 1) # start with yesterday
    day_count = 90 # go back this many days
    month_name_dict = {
        1: 'january',
        2: 'february',
        3: 'march',
        4: 'april',
        5: 'may',
        6: 'june',
        7: 'july',
        8: 'august',
        9: 'september',
        10: 'october',
        11: 'november',
        12: 'december'
    }
    while day_count > 0:
        domain = "https://the-foxfamily.blogspot.com"
        day_name = str(day.day) + "-" + month_name_dict[day.month]
        url = domain + "/" + str(day.year) + "/" + pad_left(str(day.month), "0", 2) + "/" + day_name + ".html"
        response = requests.get(url, headers=headers)
        response.close()
        links = get_img_links(response.text)
        for counter, link in enumerate(links):
            download(link, "img_" + day_name + "_" + str(counter) + ".jpg")
        day = day - timedelta(days = 1)
        day_count -= 1;

run()
