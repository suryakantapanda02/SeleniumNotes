from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


service_obj = Service('C:\\chromedriver\\chromedriver\\chromedriver.exe')

driver = webdriver.Chrome(service=service_obj)

driver.get('file:///C:/Users/admin/PycharmProjects/TreenetraClass/AutomationProjectClass1/Selenium/test_check.html?firstName=chvjhkvhvj&lastName=guivhvhg&age=35-44&gender=male')

first_name= driver.find_element(By.ID,"firstName")
first_name.send_keys('Gupta Prasad')

last_name = driver.find_element(By.NAME,"lastName")
last_name.send_keys('Samal')

time.sleep(5)


