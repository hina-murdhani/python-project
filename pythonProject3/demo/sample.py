import time

from selenium import webdriver
driver=webdriver.Chrome(r"C:\Users\hina.murdhani\PycharmProjects\pythonProject3\Browser\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("javatpoint")
time.sleep(3)
driver.find_element_by_name("btnK").click()
driver.close()
