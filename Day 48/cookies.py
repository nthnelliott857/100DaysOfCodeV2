from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

MINUTES = 5

chrome_driver_path = r"C:\Users\nthne\OneDrive\OneDrive-UW\UW-OneDrive\Documents\100 Days of Python\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")


def play_cookie_game():
    time_out = MINUTES * 60
    timeout_start = time.time()

    while time.time() < timeout_start + time_out:
        loop()
        buy_item()
    print_stats()


def buy_item():
    element_updates = driver.find_elements(By.CSS_SELECTOR, "b")
    update_list = [item.text.split("-") for item in element_updates if len(item.text.split("-")) > 1]
    money_element = driver.find_element(By.ID, "money")
    money = money_element.text
    money = int("".join(money.split(",")))
    item_to_buy = ""

    location = 0
    for i in range(0, len(update_list)):
        if int(update_list[0][1]) <= money:
            if len(update_list[i]) < 2 or int("".join(update_list[i][1].split(","))) > money:
                item_to_buy = update_list[i - 1][0]
                location = i - 1
                break

    element_to_buy = driver.find_element(By.ID, f"buy{update_list[location][0].strip()}")
    element_to_buy.click()
    print(f"{item_to_buy} purchased")


def loop():
    timeout = 5
    timeout_start = time.time()
    while time.time() < timeout_start + timeout:
        cookie.click()


def print_stats():
    cps = driver.find_element(By.ID, "cps")
    print(cps.text)


play_cookie_game()
