#from selenium.webdriver.common.keys import Keys
import unittest
from selenium import webdriver
#driver = webdriver.Firefox()
#driver= webdriver.firefox(executable_path="/home/haseeb/WebDriver/geckodriver-v0.28.0-linux64.tar.gz.asc")

driver = webdriver.Firefox()
base_url="http://book.theautomatedtester.co.uk/"


# Chrome(executable_path='/home/haseeb/WebDriver/geckodriver-v0.28.0-linux64.tar.gz.asc')


driver.maximize_window()

driver.implicitly_wait(10) #10 is in seconds

driver.get(base_url)
 
#driver.find_element_by_link_text("/chapter1").click()

driver.find_elements_by_xpath('/html/body/div[2]/ul/li[1]/a')[0].click()

#text_search = driver.find_element_by_class_name('leftdiv')

text_search = driver.find_element_by_xpath('//*[@id="divontheleft"]')

#assert "Assert that this text is on the page" in text_search

assert text_search.text == 'Assert that this text is on the page'
print(text_search.text + ' is present on chapter 1 page ')

#assert text_search.get_attribute('text') == 'Assert that this text is on the page'



driver.implicitly_wait(10) #10 is in seconds

# assert text_search.text == 'Assert that this text is on the page'

#driver.find_elements_by_xpath('/html/body/div[2]/p[4]/a').click()

driver.find_element_by_partial_link_text("Home Page").click()

driver.implicitly_wait(10) #10 is in seconds


driver.close()
