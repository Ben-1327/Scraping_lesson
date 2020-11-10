from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('/usr/local/Caskroom/chromedriver/86.0.4240.22/chromedriver')

driver.get('https://www.google.co.jp')


search_bar = driver.find_element_by_name("q")
search_bar.send_keys("python")
search_bar.submit()
