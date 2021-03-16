from selenium import webdriver
from parsel import Selector
from csv import writer
import time
import sys


sys.setrecursionlimit(10**6)
 
url = ("https://www.tripadvisor.com/Restaurants-g187851-Piedmont.html")

driver = webdriver.Chrome('chromedriver.exe')


driver.get(url)
driver.maximize_window()
driver.execute_script("window.scrollBy(0,500)","")
time.sleep(1)
driver.execute_script("window.scrollBy(0,1200)","")
time.sleep(1)
driver.execute_script("window.scrollBy(0,1700)","")
time.sleep(1)


#button = driver.find_element_by_xpath("(//button[@class='evidon-banner-acceptbutton'])")
#if button:
  #  button.click()
 #   time.sleep(1)

geo_wrap = driver.find_element_by_xpath("//div[@class='geo_wrap']")
geo_wrap.click()
print("geo_wrap", geo_wrap)

def Extract():
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(5)

  
    driver.execute_script("window.scrollBy(0,300)","")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0,600)","")
    time.sleep(1)
    
    sel = Selector(text=driver.page_source)
    
    url = driver.current_url
    
    try:
        Name = sel.xpath("//div[@class='_1hkogt_o']//h1[1]/text()").extract_first().strip()
    except:
        Name = "empty"
    try:
        address = sel.xpath("(//a[@class='_15QfMZ2L'])[2]/text()").extract_first().strip()
    except:
        address = "empty"
    try:
        review = sel.xpath("//a[@class='_3S6pHEQs']//span[1]/text()").extract_first().strip()
    except:
        review = "empty"
    try:
        rating = sel.xpath("//div[@class='Ct2OcWS4']//span/text()").extract_first().strip()
    except:
        rating = "empty"
    try:     
        excelent = sel.xpath("(//span[contains(@class,'row_num ')])[1]/text()").extract_first().strip()
    except:
        excelent = "empty"
    try:
        verygood = sel.xpath("(//span[contains(@class,'row_num ')])[2]/text()").extract_first().strip()
    except:
        verygood = "empty"
    try:
        Average = sel.xpath("(//span[contains(@class,'row_num ')])[3]/text()").extract_first().strip()
    except:
        Average = "empty"
    try:
        poor = sel.xpath("(//span[contains(@class,'row_num ')])[4]/text()").extract_first().strip()
    except:
        poor = "empty"
    try:
        teriable = sel.xpath("(//span[contains(@class,'row_num ')])[5]/text()").extract_first().strip()
    except:
        teriable = "empty"
        
        
    
    print(url)
    print(Name)
    print(address)
    print(review)
    print(rating)
    print(excelent)
    print(verygood)
    print(Average)
    print(poor)
    print(teriable)



    #inserting data in CSV***
      
    print("Exporting to CSV...Done")

    def append_list_as_row(file_name, list_of_elem):
        with open(file_name, 'a+', newline='', encoding='utf8') as write_obj:
            csv_writer = writer(write_obj)
            csv_writer.writerow(list_of_elem)
    row_contents = [url , Name , address , review , rating , excelent , verygood , Average , poor , teriable ]
    append_list_as_row('restaurants_Piedmont.csv', row_contents)


    driver.close()
    driver.switch_to.window(driver.window_handles[0])
        





def name_fun():

    name_1 = driver.find_element_by_xpath("//div[@class='wQjYiB7z']//a")
    print("Name", name_1)
    for name in name_1:
        try:
            name.click()
            Extract()
        
        except:
            print("not found")
        
    
    
name_fun()




