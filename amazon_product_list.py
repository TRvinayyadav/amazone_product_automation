from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_object = Service()
driver = webdriver.Chrome(service=service_object)

#this is a test code 

driver.get("https://www.amazon.in/")
driver.find_element(By.XPATH, "//*[@id='nav-xshop']/a[4]").click()
driver.sleep(10)

product_list= driver.find_elements(By.XPATH, "//div[@class='_octopus-search-result-card_style_apbSearchResultItem__2-mx4']")
#
for product in product_list:
#     with open('abc.csv','a+') as file:
#         file.write(product.text)


    with open('abc.csv', 'a+' , encoding='utf-8') as file:
        file.write(product.text + '\n')

print("Hello Tanvi!")

driver.quit()
