import time
# import the webdriver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
# define the chrome driver path
driver = webdriver.Chrome(r"C:\Users\hina.murdhani\PycharmProjects\pythonProject3\Browser\chromedriver.exe")
# to maximize the chrome window
driver.maximize_window()
# to point out particular url
driver.get("https://qa-hire.scikey.ai/hirer/login")
# for finding the elements on page
elements = driver.find_elements_by_tag_name("input")
print(elements)
# For the link text use single quote
# element1 = driver.find_element_by_link_text('Forgot Password?')
# print(element1)
# element1.click()
# for writing text in input field
driver.find_element_by_name("email").send_keys("dinal.mandaviya@srkaycg.com")
time.sleep(3)
driver.find_element_by_name("password").send_keys("12345678")
time.sleep(2)
elem = driver.find_element_by_xpath("//button[contains(text(),'Sign In')]")

# to perform action on element
action = ActionChains(driver)
action.move_to_element(elem)
action.click(elem)
# action.click(on_element = element)
action.perform()
# driver.find_element_by_xpath("//button[contains(text(),'Sign In')]").click()
time.sleep(3)
# driver.find_element_by_name("b").send_keys(Keys.ENTER)
# for close the Window
driver.close()
