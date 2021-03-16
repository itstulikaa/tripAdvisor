from selenium import webdriver
from parsel import Selector
from csv import writer
import time
import sys


sys.setrecursionlimit(10**6)


url = ("https://www.tripadvisor.com/Hotels-g187851-Piedmont-Hotels.html")
driver = webdriver.Chrome('chromedriver.exe')


driver.get(url)
driver.maximize_window()
time.sleep(8)

button = driver.find_element_by_xpath("(//button[@class='evidon-banner-acceptbutton'])")
if button:
    button.click()
    time.sleep(1)



#date_in = driver.find_element_by_xpath("(//div[@class='isgB-Yem '])[1]")
#date_in.click()
#time.sleep(1)

#date_out = driver.find_element_by_xpath("(//div[@class='isgB-Yem low'])[2]")
#date_out.click()
#time.sleep(1)

#update = driver.find_element_by_xpath("//*[@id='PERSISTENT_TRIP_SEARCH_BAR']/div[1]/div/div/div[2]/button")
#update.click()
#time.sleep(2)



def Extract():
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(3)
 
    driver.execute_script("window.scrollBy(0,300)","")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0,500)","")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0,700)","")
    time.sleep(1)
    driver.execute_script("window.scrollBy(0,1200)","")
    time.sleep(2)
    
    


    sel = Selector(text=driver.page_source)
    
    url = driver.current_url
    
    try:
        Name = sel.xpath("//div[contains(@class,'ui_column is-12-tablet')]//h1[1]/text()").extract_first().strip()
    except:
        Name = "empty"   
    try:
        review = sel.xpath("//a[@class='_15eFvJyR _3nlVsadw']/span[@class='_33O9dg0j']/text()").extract_first().strip()
    except:
        review = "empty"

    try:
        detail = sel.xpath("//b[@class='rank']/following-sibling::a[1]/text()").extract_first().strip()
    except:
        detail = "empty"

    try:
        Rating = sel.xpath("//div[@class='kVNDLtqL']/span/text()").extract_first().strip()
    except:
        Rating = "empty"
    try:
        Rating_text = sel.xpath("//a[@class='_1dCQBg5N']//div[1]/text()").extract_first().strip()
    except:
        Rating_text = "empty"
    try:
        excelent = sel.xpath("(//span[@class='_3fVK8yi6'])[1]/text()").extract_first().strip()
    except:
        excelent = "empty"
    try:
        verygood = sel.xpath("(//span[@class='_3fVK8yi6'])[2]/text()").extract_first().strip()
    except:
        verygood = "empty"
    try:
        Average = sel.xpath("(//span[@class='_3fVK8yi6'])[3]/text()").extract_first().strip()
    except:
        Average = "empty"
    try:
        poor = sel.xpath("(//span[@class='_3fVK8yi6'])[4]/text()").extract_first().strip()
    except:
        poor = "empty"
    try:
        teriable = sel.xpath("(//span[@class='_3fVK8yi6'])[5]/text()").extract_first().strip()
    except:
        teriable = "empty"

    try:
        english = sel.xpath("(//span[@class='mxlinKbW'])[2]/text()").extract_first().strip()
    except:
        english = "empty"
    try:
        french = sel.xpath("(//span[@class='mxlinKbW'])[3]/text()").extract_first().strip()
    except:
        french = "empty"

    try:
        dutch = sel.xpath("(//span[@class='mxlinKbW'])[4]/text()").extract_first().strip()
    except:
        dutch = "empty"
    
    try:
        language_1 = sel.xpath("(//span[@class='_1wk-I7LS'])[2]/text()").extract_first().strip()
    except:
        language_1 = "empty"
    
    try:
        language_2 = sel.xpath("(//span[@class='_1wk-I7LS'])[3]/text()").extract_first().strip()
    except:
        language_2 = "empty"
    
    try:
        language_3 = sel.xpath("(//span[@class='_1wk-I7LS'])[4]/text()").extract_first().strip()
    except:
        language_3 = "empty"
    
    try:
        address = sel.xpath("//span[@class='_3ErVArsu jke2_wbp']/text()").extract_first().strip()
    except:
        address = "empty"
    
    
    print(url)
    print(Name)
    print(review)
    print(detail)
    print(Rating)
    print(Rating_text)
    print(excelent)
    print(verygood)
    print(Average)
    print(poor)
    print(teriable)
    print(english)
    print(french)
    print(dutch)
    print(language_1)
    print(language_2)
    print(language_3)
    print(address)
    



    #inserting data in CSV***
      
    print("Exporting to CSV...Done")

    def append_list_as_row(file_name, list_of_elem):
        with open(file_name, 'a+', newline='', encoding='utf8') as write_obj:
            csv_writer = writer(write_obj)
            csv_writer.writerow(list_of_elem)
    row_contents = [url, Name , review , detail , Rating , Rating_text , excelent , verygood , Average , poor , teriable , language_1 + " " + english ,language_2 + " " + french ,language_3 + " " + dutch, address]
    append_list_as_row('Hotels_output.csv', row_contents)



    driver.close()
    driver.switch_to.window(driver.window_handles[0])


def Name_fun():

    try:
        name_1 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[1]")
        name_1.click()

        Extract()
    except:
        print("name_1")    

    try:
        name_2 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[2]")
        name_2.click()

        Extract()
    except:
        print("name_2")

    try:    
        name_3 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[3]")
        name_3.click()

        Extract()
    except:
        print("name_3")

    try:
        name_4 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[4]")
        name_4.click()

        Extract()
    except:
        print("name_4")

    try:
        name_5 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[5]")
        name_5.click()

        Extract()
    except:
        print("name_5")
          
    try:
        name_6 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[6]")
        name_6.click()

        Extract()
    except:
        print("name_6")

    try:
        name_7 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[7]")
        name_7.click()

        Extract()
    except:
        print("name_7")

    try:
        name_8 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[8]")
        name_8.click()

        Extract()
    except:
        print("name_8")

    try:
        name_9 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[9]")
        name_9.click()

        Extract()
    except:
        print("name_9") 

    try:
        name_10 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[10]")
        name_10.click()

        Extract()
    except:
        print("name_10")

        
    try:
        name_11 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[11]")
        name_11.click()

        Extract()
    except:
        print("name_11")    
        

        
    try:
        name_12 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[12]")
        name_12.click()

        Extract()
    except:
        print("name_12")    
        

        
    try:
        name_13 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[13]")
        name_13.click()

        Extract()
    except:
        print("name_13")    
        

        
    try:
        name_14 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[14]")
        name_14.click()

        Extract()
    except:
        print("name_14")    
        

        
    try:
        name_15 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[15]")
        name_15.click()

        Extract()
    except:
        print("name_15")    
        

        
    try:
        name_16 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[16]")
        name_16.click()

        Extract()
    except:
        print("name_16")    
        

        
    try:
        name_17 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[17]")
        name_17.click()

        Extract()
    except:
        print("name_17")    
        

        
    try:
        name_18 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[18]")
        name_18.click()

        Extract()
    except:
        print("name_18")    
        

        
    try:
        name_19 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[19]")
        name_19.click()

        Extract()
    except:
        print("name_19")    
        

        
    try:
        name_20 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[20]")
        name_20.click()

        Extract()
    except:
        print("name_20")    

        
    try:
        name_21 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[21]")
        name_21.click()

        Extract()
    except:
        print("name_21")

        
    try:
        name_22 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[22]")
        name_22.click()

        Extract()
    except:
        print("name_22")

        
    try:
        name_23 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[23]")
        name_23.click()

        Extract()
    except:
        print("name_23")


        
    try:
        name_24 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[24]")
        name_24.click()

        Extract()
    except:
        print("name_24")

        
    try:
        name_25 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[25]")
        name_25.click()

        Extract()
    except:
        print("name_25")        

        
    try:
        name_26 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[26]")
        name_26.click()

        Extract()
    except:
        print("name_26")        
        
    try:
        name_27 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[27]")
        name_27.click()

        Extract()
    except:
        print("name_27")        
        
    try:
        name_28 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[28]")
        name_28.click()

        Extract()
    except:
        print("name_28")        
        
    try:
        name_29 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[29]")
        name_29.click()

        Extract()
    except:
        print("name_29")        
        
    try:
        name_30 = driver.find_element_by_xpath("(//a[@class='property_title prominent '])[30]")
        name_30.click()

        Extract()
    except:
        print("name_30")
        
        

Name_fun()


Next_button_1 = driver.find_element_by_xpath("(//div[contains(@class,'unified ui_pagination')]//a)[1]")
Next_button_1.click()
time.sleep(10)
Name_fun()




