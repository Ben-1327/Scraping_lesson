from bs4 import BeautifulSoup
import requests


keyword = 'Python スクレイピング'
url = "https://www.amazon.co.jp/s?k=" + keyword + "&__mk_ja_JP=カタカナ&ref=nb_sb_noss_1"

html = requests.get(url)
soup = BeautifulSoup(html.text, "lxml")

items = soup.select(".sg-col-inner")

for item in items:
    item_text = "".join(item.text)
    print(item_text)
