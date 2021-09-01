#Cookies Generator - Generates the cookies.pkl
#I uses a temp mail account, edit your own email and password here.


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import os
import time
import pickle

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.instagram.com/accounts/login/")

time.sleep(5)

username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
username.send_keys('papiw49218@mi166.com')

password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
password.send_keys('Hello@123')

login_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
login_button.click()
time.sleep(10)

driver.get_screenshot_as_file("home.png")

pickle.dump( driver.get_cookies() , open("cookies.pkl","wb"))

driver.quit()