import csv
from selenium import webdriver # pip install selenium , webdriver to intract with web browser
from selenium.common.exceptions import NoSuchElementExceptionth 
import os

chromedriver = 'F:\\Users\\Deep\\Desktop\\chromedriver.exe' # chrome exe file path
os.environ["webdriver.chrome.driver"] = chromedriver # to set environment variable

data=[]
page_nos=[ x for x in range(1,26)]
driver = webdriver.Chrome(chromedriver)
driver.implicitly_wait(5)
driver2 = webdriver.Chrome(chromedriver)
driver2.implicitly_wait(5)


try:
        
    for traverse in page_nos:
        listing_page="https://www.zomato.com/ncr/noida-restaurants" + "?page=" + str(traverse)
        print(listing_page)
        driver.get(listing_page)
        elem = driver.find_elements_by_class_name("result-title")
        for restaurants in elem:
            link=restaurants.get_attribute("href")
            name=restaurants.text
            driver2.get(link)
            try:
                telno=driver2.find_element_by_class_name("tel").text.replace("\n"," and ")
                address=driver2.find_element_by_class_name("res-main-address-text").text.replace('<span>',"").replace("</span>","")
                rating=driver2.find_element_by_class_name("rating-div").text
            except NoSuchElementException as e:
                print(e)
                print(listing_page + link)
            entry={'Name': name,'Telno' : telno, 'Address' : address, 'Rating': rating}
            print(entry)
            data.append(entry)
except Exception as e:
    print(e)
    print(listing_page + link)
    
        
driver.close()


sorte=sorted(data,key = lambda restaurant : restaurant['Name'])

with open('paiwallah_noida.csv', 'w') as csvfile:
    fieldnames = ['Name','Telno','Address','Rating']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for entries in sorte:
        writer.writerow(entries)


        







