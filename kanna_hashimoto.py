from bs4 import BeautifulSoup
import requests
import urllib.request
import random

html = requests.get("http://iam-publicidad.org/article/1000%E5%B9%B4%E3%81%AB%E4%B8%80%E5%BA%A6%E3%81%AE%E9%80%B8%E6%9D%90%EF%BC%81%E6%A9%8B%E6%9C%AC%E7%92%B0%E5%A5%88%E3%81%A1%E3%82%83%E3%82%93%E3%81%AE%E5%8F%AF%E6%84%9B%E3%81%8F%E3%81%A6%E5%A4%A9")
soup = BeautifulSoup(html.text, "lxml")

for link in soup.select("#content img"):
    try:
        src = link.get("src")
        print(src)
        img_name = random.randrange(1,100)
        full_name = str(img_name) + ".jpg"
        urllib.request.urlretrieve(src, full_name)
    except:
        pass
