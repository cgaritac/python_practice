from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

service = Service(executable_path='Drivers/msedgedriver.exe')
driver = webdriver.Edge(service=service)
driver.get('https://www.selenium.dev/documentation/webdriver/elements/')

link_recovery = driver.find_element(By.PARTIAL_LINK_TEXT, 'WebD')
link_recovery.click()
time.sleep(2)

driver.quit()