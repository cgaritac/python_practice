from selenium import webdriver
from selenium.webdriver.edge.service import Service

service = Service(executable_path='Drivers/msedgedriver.exe')

driver = webdriver.Edge(service=service)
driver.maximize_window()

driver.get("https://www.google.com")

driver.close()