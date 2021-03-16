from selenium import webdriver
from parsel import Selector
from csv import writer
import time
import sys 
import pyodbc
import xlrd

#server = '176.9.106.48'
#database = 'blackcircles'
#username = 'sa'
#password = '$u7Br0h0ws'
#cnxn = pyodbc.connect(
#    'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
#cursor = cnxn.cursor()

#def dbConnection():

 #   dataSQL = cursor.execute(
#        "select * from trip_restaurant")
#    rows = cursor.fetchall()
#    return rows
# #sys.exit() 

#keySQL = dbConnection()



sys.setrecursionlimit(10**6)
 
#url = ("https://www.tripadvisor.com/Restaurants-g187851-Piedmont.html")

loc = ('C:\\Users\\Loginworks\\Desktop\\Tripadvisor\\republic_dominica_cities.xlsx')
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)
url = (sheet.cell_value(0, 0))

print(url)
    

driver = webdriver.Chrome('chromedriver.exe')


driver.get(url)
driver.maximize_window()
driver.execute_script("window.scrollBy(0,500)","")
time.sleep(1)
driver.execute_script("window.scrollBy(0,1200)","")
time.sleep(1)
driver.execute_script("window.scrollBy(0,1700)","")
time.sleep(1)





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
    append_list_as_row('restaurants_repulic_dominica.csv', row_contents)


    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    





def name_fun():
    try:
        name_1 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[2]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_1.click()
        Extract()
    except:
        print("name_1")
    
    try:
        name_2 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[3]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_2.click()
        Extract()
    except:
        print("name_2")

    try:    
        name_3 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[4]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_3.click()

        Extract()
    except:
        print("name_3")

    try:    
        name_4 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[6]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_4.click()

        Extract()
    except:
        print("name_4")

    try:    
        name_5 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[7]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_5.click()

        Extract()
    except:
        print("name_5")
    
    try:
        name_6 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[9]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_6.click()

        Extract()
    except:
        print("name_6")

    try:    
        name_7 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[10]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_7.click()

        Extract()
    except:
        print("name_7")

    try:    
        name_8 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[11]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_8.click()

        Extract()
    except:
        print("name_8")

    try:    
        name_9 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[13]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_9.click()

        Extract()
    except:
        print("name_9")

    try:
        name_10 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[14]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_10.click()

        Extract()
    except:
        print("name_10")
    try:
        name_11 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[15]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_11.click()

        Extract()
    except:
        print("name_11")
     
    try:
        name_12 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[16]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_12.click()

        Extract()
    except:
        print("name_12")

    try:
        name_13 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[17]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_13.click()

        Extract()
    except:
        print("name_13")
     
    try:
        name_14 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[18]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_14.click()

        Extract()
    except:
        print("name_14")
    try:
        name_15 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[19]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_15.click()
    
        Extract()
    except:
        print("name_15")

    try:
        name_16 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[21]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_16.click()

        Extract()
    except:
        print("name_16")

    try:
        name_17 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[22]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_17.click()

        Extract()
    except:
        print("name_17")  

    try:
        name_18 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[24]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_18.click()

        Extract()
    except:
        print("name_18")

    try:
        name_19 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[25]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_19.click()

        Extract()
    except:
        print("name_19")

    try:
        name_20 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[26]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_20.click()

        Extract()
    except:
        print("name_20")

    try:
        name_21 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[28]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_21.click()

        Extract()
    except:
        print("name_21")

    try:
        name_22 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[29]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_22.click()

        Extract()
    except:
        print("name_22")


    try:
        name_23 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[31]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_23.click()

        Extract()
    except:
        print("name_23")


    try:
        name_24 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[32]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_24.click()

        Extract()
    except:
        print("name_24")

    try:
        name_25 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[33]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_25.click()

        Extract()
    except:
        print("name_25")


    try:
        name_26 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[34]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_26.click()

        Extract()
    except:
        print("name_26")

    try:
        name_27 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[35]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_27.click()

        Extract()
    except:
        print("name_27")

    try:
        name_28 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[36]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_28.click()

        Extract()
    except:
        print("name_28")

    try:
        name_29 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[38]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_29.click()

        Extract()
    except:
        print("name_29")

    try:
        name_30 = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[39]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_30.click()

        Extract()

    except:
        print("name_30")



    try:
        name_A = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[1]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_A.click()

        Extract()
    except:
        print("name_A")

    try:     
        name_B = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[5]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_B.click()

        Extract()
    except:
        print("name_B")


    try:      
        name_c = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[8]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_c.click()

        Extract()
    except:
        print("name_c")

    try:    
        name_d = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[12]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_d.click()

        Extract()
    except:
        print("name_d")

    try:     
        name_e = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[20]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_e.click()

        Extract()
    except:
        print("name_e")


    try:   
        name_f = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[23]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_f.click()

        Extract()
    except:
        print("name_f")

    try: 
        name_g = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[27]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_g.click()

        Extract()
    except:
        print("name_g")

    try:   
        name_h = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[30]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_h.click()

        Extract()
    except:
        print("name_h")

    try:     
        name_i = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[37]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_i.click()

        Extract()

    except:
        print("name_i")
        
    try:     
        name_k = driver.find_element_by_xpath("//div[@id='component_2']/div[1]/div[37]/span[1]/div[1]/div[2]/div[1]/div[1]/span[1]/a[1]")
        name_k.click()

        Extract()

    except:
        print("name_k") 

   



name_fun()

Next_button = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[1]")
Next_button.click()
time.sleep(20)

name_fun()

Next_2 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_2.click()
time.sleep(20)

name_fun()

Next_3 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_3.click()
time.sleep(20)

name_fun()

Next_4 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_4.click()
time.sleep(20)

name_fun()

Next_5 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_5.click()
time.sleep(20)

name_fun()

Next_6 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_6.click()
time.sleep(20)

name_fun()

Next_7 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_7.click()
time.sleep(20)

name_fun()

Next_8 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_8.click()
time.sleep(20)

name_fun()

Next_9 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_9.click()
time.sleep(20)

name_fun()

Next_10 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_10.click()
time.sleep(20)

name_fun()

Next_11 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_11.click()
time.sleep(20)

name_fun()

Next_12 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_12.click()
time.sleep(20)

name_fun()

Next_13 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_13.click()
time.sleep(20)

name_fun()

Next_14 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_14.click()
time.sleep(20)

name_fun()

Next_15 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_15.click()
time.sleep(20)

name_fun()

Next_16 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_16.click()
time.sleep(20)

name_fun()

Next_17 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_17.click()
time.sleep(20)

name_fun()

Next_18 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_18.click()
time.sleep(20)

name_fun()

Next_19 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_19.click()
time.sleep(20)

name_fun()

Next_20 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_20.click()
time.sleep(20)

name_fun()

Next_21 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_21.click()
time.sleep(20)

name_fun()

Next_22 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_22.click()
time.sleep(20)

name_fun()

Next_23 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_23.click()
time.sleep(20)

name_fun()

Next_24 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_24.click()
time.sleep(20)

name_fun()

Next_25 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_25.click()
time.sleep(20)

name_fun()

Next_26 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_26.click()
time.sleep(20)

name_fun()

Next_27 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_27.click()
time.sleep(20)

name_fun()

Next_28 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_28.click()
time.sleep(20)

name_fun()


Next_29 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_29.click()
time.sleep(20)

name_fun()


Next_30 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_30.click()
time.sleep(20)

name_fun()


Next_31 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_31.click()
time.sleep(20)

name_fun()



Next_32 = driver.find_element_by_xpath("(//div[contains(@class,'unified pagination')]//a)[2]")
Next_32.click()
time.sleep(20)

name_fun()







