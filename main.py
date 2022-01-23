from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from .credential import username, password

op = webdriver.ChromeOptions()
op.add_argument('headless')
s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(options=op, service=s)

url = "https://zenius.darwinbox.com"

# Login Page
driver.get(url)
time.sleep(2)
username_field = driver.find_element(By.ID, 'UserLogin_username')
username_field.send_keys(username)
password_field = driver.find_element(By.ID, 'UserLogin_password')
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)
time.sleep(2)

skip = driver.find_element(By.CLASS_NAME, 'skip_pulse')
if skip.text != "":
    skip.click()

# clockin
clockin_btn = driver.find_element_by_id('attendance-logger-widget')
clockin_btn.clear()
time.sleep(2)

#Signout
driver.get(url + "/user/logout")
time.sleep(1)

#Close Chrome
driver.quit()

print('berhasil yes')