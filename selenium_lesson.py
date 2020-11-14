from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import csv
import datetime

options = Options()
# options.add_argument('--headless')
driver = webdriver.Chrome('/usr/local/Caskroom/chromedriver/86.0.4240.22/chromedriver',options=options)
driver.get('https://www.google.co.jp')


search_bar = driver.find_element_by_name("q")
search_bar.send_keys("python")
search_bar.submit()


csv_date = datetime.datetime.today().strftime("%Y%m%d")
csv_file_name = 'google_python_' + csv_date + '.csv'
f = open(csv_file_name, 'w', encoding='cp932', errors='ignore')
writer = csv.writer(f, lineterminator='\n')
csv_header = ["検索順位","URL","サマリー"]
writer.writerow(csv_header)


i = 1
item = 1
while True:
    i = i + 1
    sleep(1)
    for elem_h3 in driver.find_elements_by_xpath('//a/h3'):
        elem_a = elem_h3.find_element_by_xpath('..')
        csvlist = []
        csvlist.append(str(item))
        csvlist.append(elem_h3.text)
        csvlist.append(elem_a.get_attribute('href'))
        writer.writerow(csvlist)
        item = item + 1
    next_link = driver.find_element_by_id('pnnext')
    driver.get(next_link.get_attribute('href'))
    if i >= 6:
        break

f.close()
driver.close()
