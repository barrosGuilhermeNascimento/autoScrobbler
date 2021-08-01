from selenium import webdriver
from selenium.webdriver.remote import webelement
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import dotenv
import time
import os
import pyautogui

dotenv.load_dotenv()
lastPass = os.getenv("LASTFMPASSWORD")

driver = webdriver.Firefox(executable_path='./.driver/geckodriver.exe')

driver.get('https://simplescrobble.com')
time.sleep(1)
driver.find_element_by_xpath('/html/body/app-root/main/app-login/button/span').click()


login: WebElement = driver.find_element_by_xpath('//*[@id="id_username_or_email"]')
login.send_keys("barrosguilherme6@outlook.com")

password = driver.find_element_by_xpath('//*[@id="id_password"]')
password.send_keys(lastPass)

driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[5]/div[2]/div/div/form/div[3]/div/button').click()
driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[5]/div[3]/div/div/section/form/div/div/button').click()

time.sleep(1)

searchbar: WebElement = driver.find_element_by_xpath('//*[@id="mat-input-0"]')
searchbar.click()
searchbar.send_keys('when - dodie')
driver.find_element_by_xpath('/html/body/app-root/main/app-search/form/button').click()

time.sleep(5)

while True:
    driver.find_element_by_xpath('/html/body/app-root/main/app-search/app-list-view/mat-nav-list/mat-list-item[1]/div').click()
    time.sleep(0.5)
    buttonPosition = pyautogui.locateOnScreen('searchButton.png')
    print(buttonPosition)
    pyautogui.click(buttonPosition)
    time.sleep(0.5)