import json
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

TWITTER_EMAIL = "WallaceWerty"
TWITTER_PASSWORD = "bPaT!MWbsSj877r"
PROMISED_DOWN = 100
PROMISED_UP = 10

class InternetSpeedTwitterBot:
    def __init__(self):
        CHROME_DRIVER_PATH = r"C:\Users\nthne\OneDrive\OneDrive-UW\UW-OneDrive\Documents\100 Days of Python\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.up = None
        self.down = None

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(By.CSS_SELECTOR, '[class="js-start-test test-mode-multi"]')
        go_button.click()
        time.sleep(45)
        self.up = self.driver.find_element(By.CSS_SELECTOR,
                                           '[class="result-data-large number result-data-value download-speed"]').text
        print(f"Upload Speed: {self.up} Mbps")
        self.down = self.driver.find_element(By.CSS_SELECTOR,
                                             '[class="result-data-large number result-data-value upload-speed"]').text
        print(f"Download Speed: {self.down} Mbps")
        #self.driver.close()

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(5)
        username_field = self.driver.find_element(By.CSS_SELECTOR,
                                                  '[class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')
        next_button = self.driver.find_element(By.CSS_SELECTOR,
                                               '[class="css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-13qz1uu"]')
        username_field.send_keys(TWITTER_EMAIL)
        next_button.click()
        time.sleep(1)
        password_field = self.driver.find_element(By.CSS_SELECTOR,
                                                  '[class="r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"]')
        password_field.send_keys(TWITTER_PASSWORD)
        login_button = self.driver.find_element(By.CSS_SELECTOR,
                                                '[class="css-18t94o4 css-1dbjc4n r-1m3jxhj r-sdzlij r-1phboty r-rs99b7 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr"]')
        login_button.click()
        time.sleep(5)
        tweet_field = self.driver.find_element(By.CSS_SELECTOR, '[class="notranslate public-DraftEditor-content"]')
        message = f"Hey LocalTel, why is my internet speed {self.down}Mbps down/{self.up} Mbps up when I pay for {PROMISED_DOWN} Mbps down/{PROMISED_UP} Mbps up?"
        tweet_field.send_keys(message)
        tweet_button = self.driver.find_element(By.CSS_SELECTOR, '[class="css-18t94o4 css-1dbjc4n r-l5o3uw r-42olwf r-sdzlij r-1phboty r-rs99b7 r-19u6a5r r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr"]')
        tweet_button.click()

