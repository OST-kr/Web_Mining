import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv

driver = webdriver.Chrome()
driver.get("https://www.zipbanchan.co.kr/shop/goods/goods_list.php")
driver.implicitly_wait(5)

items = driver.find_elements(By.CSS_SELECTOR, ".card-vertical__content")

f = open(r"C:\OST\data2.csv", 'w', encoding="CP949", newline='')

csvWriter = csv.writer(f)

for item in items:
    name = item.find_element(By.CSS_SELECTOR, ".card-content__title").text
    price = item.find_element(By.CSS_SELECTOR, ".card-content__price-discount").text
    print(name)
    print(price)
    csvWriter.writerow([name, price])

f.close()











