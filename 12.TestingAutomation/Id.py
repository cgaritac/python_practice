from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

service = Service(executable_path='Drivers/msedgedriver.exe')
controller = webdriver.Edge(service=service)
controller.get("https://kidstechskills.com/login-simulator/")
time.sleep(1)

user = controller.find_element(By.ID,"username")
password = controller.find_element(By.ID,"password")
time.sleep(1)

user.send_keys("cgaritac@gmail.com")
time.sleep(5)
password.send_keys("123456")
time.sleep(5)

button = controller.find_element(By.ID,"loginButton")
button.click()
time.sleep(5)

controller.quit()

