#test_url => http://kennethhutw.github.io/demo/Selenium/index.html

#part1
from selenium import webdriver
import time
path ="chromedriver.exe"

driver = webdriver.Chrome(path)
driver.get("http://kennethhutw.github.io/demo/Selenium/Signin.html")

#part1
driver.find_element_by_id('Signin').click()
alert = driver.find_element_by_class_name('alert-danger')
print('sign in without username and password')
print(alert.text)
time.sleep(3)

driver.find_element_by_id('username').send_keys('kenneth')
driver.find_element_by_id('password').send_keys('password')
driver.find_element_by_id('Signin').click()
print('input corrected username and password')
success = driver.find_element_by_class_name('alert-success')
print(success.text)
time.sleep(3)

driver.close()
driver.quit()

