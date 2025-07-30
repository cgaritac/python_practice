from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

service = Service(executable_path='Drivers/msedgedriver.exe')
driver = webdriver.Edge(service=service)
driver.get('https://websim.com/@Atlo81/google-login-simulator')

usuario = driver.find_element(By.XPATH, "//input[@id='emailField']")
usuario.send_keys('cgarita@gmail.com')
time.sleep(1)

password = driver.find_element(By.XPATH, "//input[@id='passwordField']")
password.send_keys('<PASSWORD>')
time.sleep(1)

button = driver.find_element(By.XPATH, "//button[normalize-space()='Sign in']")
button.click()
time.sleep(1)

driver.quit()