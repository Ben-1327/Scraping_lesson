from bs4 import BeautifulSoup
import requests

html = requests.get("https://info.finance.yahoo.co.jp/history/?code=998407.O&sy=2020&sm=10&sd=11&ey=2020&em=11&ed=10&tm=d")
soup = BeautifulSoup(html.text, "lxml")

# print(soup.select(".boardFin td"))
for price in soup.select(".boardFin td"):
    price_text = "".join(price.text)
    print(price_text)
