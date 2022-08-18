import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

INSTAGRAM_U = "nthne857"
INSTAGRAM_PW = "v.8pPZd78J:ahx:"
target_account = "philosophysays"


class InstaFollower:

    def __init__(self):
        chrome_driver_path = r"C:\Users\nthne\OneDrive\OneDrive-UW\UW-OneDrive\Documents\100 Days of Python\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)

    def login(self):
        self.driver.get("https://www.instagram.com/")
        time.sleep(1)
        username_field = self.driver.find_element(By.NAME, 'username')
        password_field = self.driver.find_element(By.NAME, 'password')
        username_field.send_keys(INSTAGRAM_U)
        password_field.send_keys(INSTAGRAM_PW)
        login_button = self.driver.find_element(By.CSS_SELECTOR, '[class="sqdOP  L3NKy   y3zKF     "]')
        login_button.click()
        time.sleep(2)
        try:
            not_now_button = self.driver.find_element(By.CSS_SELECTOR, '[class="sqdOP yWX7d    y3zKF     "]')
        except selenium.common.exceptions.NoSuchElementException:
            print("not_now_button not found")
        else:
            not_now_button.click()
        time.sleep(2)

        try:
            turn_off_notifications_button = self.driver.find_element(By.CSS_SELECTOR, '[class="_a9-- _a9_1"]')
        except selenium.common.exceptions.NoSuchElementException:
            print("turn off notifications button not found")
        else:
            turn_off_notifications_button.click()
        self.driver.get(f"https://www.instagram.com/{target_account}/")
        time.sleep(2)

    def find_followers(self):
        followers_button = self.driver.find_element(By.CSS_SELECTOR,
                                                    '[class="oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl _a6hd"]')
        followers_button.click()
        time.sleep(3)
        pop_up_window = self.driver.find_element(By.XPATH,
                                                 '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]')
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, '[class="_aaes"]')
        for i in range(0, 10):#scrolls the follower element 10 times
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                pop_up_window)
            time.sleep(1)

    def follow(self):
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, '[class="_aaes"]')
        i = 0
        while i < 40:  # instagram seems to limit likes in a short time span to around 45
            follow_button = follow_buttons[i]
            status = follow_button.text
            if status != "Following" and status != "Requested":
                follow_button.click()
                i = i + 1
                time.sleep(1)
