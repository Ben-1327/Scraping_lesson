from bs4 import BeautifulSoup
import requests
import urllib.request
import random

html = requests.get("http://illuminaters.com/archives/8706")
soup = BeautifulSoup(html.text, "lxml")

for link in soup.select(".entry-content .aligncenter, .entry-content img.aligncenter"):
    src = link.get("src")
    print(src)
    img_name = random.randrange(1,100)
    full_name = str(img_name) + ".jpg"
    urllib.request.urlretrieve(src, full_name)
