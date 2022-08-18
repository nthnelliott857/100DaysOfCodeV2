import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from InstaFollower import InstaFollower

# chrome_driver_path = r"C:\Users\nthne\OneDrive\OneDrive-UW\UW-OneDrive\Documents\100 Days of Python\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

# def setup_instagram():
#     driver.get("https://www.instagram.com/")
#     time.sleep(1)
#     username_field = driver.find_element(By.NAME, 'username')
#     password_field = driver.find_element(By.NAME, 'password')
#     username_field.send_keys(INSTAGRAM_U)
#     password_field.send_keys(INSTAGRAM_PW)
#     login_button = driver.find_element(By.CSS_SELECTOR, '[class="sqdOP  L3NKy   y3zKF     "]')
#     login_button.click()
#     time.sleep(2)
#     try:
#         not_now_button = driver.find_element(By.CSS_SELECTOR, '[class="sqdOP yWX7d    y3zKF     "]')
#     except selenium.common.exceptions.NoSuchElementException:
#         print("not_now_button not found")
#     else:
#         not_now_button.click()
#     time.sleep(2)
#     # window_handles = driver.window_handles
#     # base_window = driver.window_handles[0]
#     # turn_on_notifications_window = driver.window_handles[1]
#     # driver.switch_to.window(turn_on_notifications_window)
#     try:
#         turn_off_notifications_button = driver.find_element(By.CSS_SELECTOR, '[class="_a9-- _a9_1"]')
#     except selenium.common.exceptions.NoSuchElementException:
#         print("turn off notifications button not found")
#     else:
#         turn_off_notifications_button.click()


instagram_follower = InstaFollower()
instagram_follower.login()
instagram_follower.find_followers()
instagram_follower.follow()
