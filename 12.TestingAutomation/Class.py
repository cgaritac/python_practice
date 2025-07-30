from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
import time

service = Service(executable_path='Drivers/msedgedriver.exe')
controller = webdriver.Edge(service=service)
controller.get("https://ogg.com.br/login/login-en.php")
time.sleep(1)

user = controller.find_element(By.NAME, "nome_usuario")
password = controller.find_element(By.NAME, "pre_senha")
time.sleep(1)

user.send_keys("cgaritac@gmail.com")
password.send_keys("123456")
time.sleep(1)

button = controller.find_element(By.CLASS_NAME, "btn")
time.sleep(1)

