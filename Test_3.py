from selenium import webdriver
import selenium.webdriver.support.ui as UI
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



#driver = webdriver.Firefox()
#driver= webdriver.firefox(executable_path="/home/haseeb/WebDriver/geckodriver-v0.28.0-linux64.tar.gz.asc")

driver = webdriver.Firefox()
base_url="http://book.theautomatedtester.co.uk/"


# Chrome(executable_path='/home/haseeb/WebDriver/geckodriver-v0.28.0-linux64.tar.gz.asc')


driver.maximize_window()

driver.implicitly_wait(10) #10 is in seconds

driver.get(base_url)
 
#driver.find_element_by_link_text("/chapter1").click()

#driver.find_element_by_xpath('/html/body/div[2]/ul/li[4]/a').click()

driver.implicitly_wait(10) #10 is in seconds

action = ActionChains(driver)

element_to_hover_over = driver.find_element_by_xpath("/html/body/div[2]/ul/li[4]/a")
action.move_to_element(element_to_hover_over).perform()

driver.implicitly_wait(20)

driver.close()
