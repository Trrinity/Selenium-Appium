from selenium import webdriver
driver =webdriver.Chrome()

driver.get('http://www.scholat.com')
print(driver.title)