
from selenium import webdriver
import selenium.webdriver.support.ui as UI
from selenium.webdriver.common.by import By


#driver = webdriver.Firefox()
#driver= webdriver.firefox(executable_path="/home/haseeb/WebDriver/geckodriver-v0.28.0-linux64.tar.gz.asc")

driver = webdriver.Firefox()
base_url="http://book.theautomatedtester.co.uk/"


# Chrome(executable_path='/home/haseeb/WebDriver/geckodriver-v0.28.0-linux64.tar.gz.asc')


driver.maximize_window()

driver.implicitly_wait(10) #10 is in seconds

driver.get(base_url)
 
#driver.find_element_by_link_text("/chapter1").click()

driver.find_element_by_xpath('/html/body/div[2]/ul/li[4]/a').click()

driver.implicitly_wait(10) #10 is in seconds

select_box = driver.find_element_by_id ("selecttype")

options = [x for x in select_box.find_elements_by_tag_name("option")]

#for element in options:
 #print element.get_attribute("value")

#for i in range(len(x)):
 #   print x[i].text

#print(len(options))
for item in options:
     print(item.text)

driver.close()
