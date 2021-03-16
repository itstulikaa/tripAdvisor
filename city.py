from selenium import webdriver
from parsel import Selector
from csv import writer
import time
import sys


sys.setrecursionlimit(10**6)
 
url = ("https://www.tripadvisor.com/Restaurants-g187851-oa20-Piedmont.html#LOCATION_LIST")

driver = webdriver.Chrome('chromedriver.exe')


driver.get(url)
driver.maximize_window()
driver.execute_script("window.scrollBy(0,500)","")
time.sleep(1)
driver.execute_script("window.scrollBy(0,1200)","")
time.sleep(1)
driver.execute_script("window.scrollBy(0,1700)","")
time.sleep(1)

sel = Selector(text=driver.page_source)

cities = sel.xpath("//ul[@class='geoList']")
for c in cities:
    city = c.xpath(".//li//a//@href").extract()
final = [all for all in city]
print("final", final)
for letter in final:
    final.append(letter)
worksheet.write_column('A1', final)
