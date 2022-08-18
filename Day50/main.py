import json

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

FB_USERNAME = "509-668-0216"
FB_PASSWORD = "Scalrtq52&!"

EMAIL = "nthnelliott857@gmail.com"
EMAIL_PASSWORD = "LogGracedPhonyHolder!3"

chrome_driver_path = r"C:\Users\nthne\OneDrive\OneDrive-UW\UW-OneDrive\Documents\100 Days of Python\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)


def setup_tinder():
    driver.get("https://tinder.com/")
    time.sleep(1)
    # button = driver.find_element(By.LINK_TEXT, 'https://tinder.onelink.me/9K8a/3d4abb81')
    button = driver.find_element(By.CSS_SELECTOR, '[class="Pos(r) Z(1) D(b) W(100%)"]')  # selects "Log In" button
    button.click()
    time.sleep(1)
    # log_in_with_google = driver.find_element(By.XPATH, '//*[@id="o-1442994379"]/div/div/div[1]/div/div/div[3]/span/div[1]/div/button')
    # log_in_with_google.click()
    # window_handles = driver.window_handles
    # base_window = driver.window_handles[0]
    # google_login_window = driver.window_handles[1]
    # driver.switch_to.window(google_login_window)
    # google_login_window_email_input = driver.find_element(By.NAME, 'identifier')
    # google_login_window_email_input.send_keys(EMAIL)
    # google_login_window_next_button = driver.find_element(By.CSS_SELECTOR, '[class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc qfvgSe qIypjc TrZEUc lw1w4b"]')
    # google_login_window_next_button.click()

    log_in_with_facebook_button = driver.find_element(By.XPATH, '//*[@id="t108358321"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')  # //*[@id="o-1442994379"]/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]')



    log_in_with_facebook_button.click()
    time.sleep(2)

    window_handles = driver.window_handles
    base_window = driver.window_handles[0]
    fb_login_window = driver.window_handles[1]
    driver.switch_to.window(fb_login_window)

    fb_username_field = driver.find_element(By.NAME, 'email')
    fb_password_field = driver.find_element(By.NAME, 'pass')
    fb_log_in_button = driver.find_element(By.NAME, 'login')
        #
    fb_username_field.send_keys(FB_USERNAME)
    fb_password_field.send_keys(FB_PASSWORD)
    fb_log_in_button.click()
    time.sleep(5)
    # try:
    # #     continue_as_nathan_button = driver.find_element(By.CSS_SELECTOR, '[class="a8c37x1j ni8dbmo4 stjgntxs l9j0dhe7 ltmttdrg g0qnabr5 ojkyduve"]')
    # # except selenium.common.exceptions.InvalidSelectorException or selenium.common.exceptions.NoSuchElementException:
    # #     print("Continue as Nathan not found")
    # # else:
    # #     continue_as_nathan_button.click()
    driver.switch_to.window(base_window)
    time.sleep(5)
    # tinder_phone_number_input = driver.find_element(By.CSS_SELECTOR, '[class="Fz($m) Va(m) Py(8px) Bdrs(4px)--ml Bgc($c-divider-lite)--ml Px(8px)--ml BdB--s Bdrs(0)--s Bdbc($c-secondary)--s Px(4px)--s D(ib) Lts($ls-m) Bdrsbstart(0)! Bdrststart(0)!"]')
    # tinder_phone_number_input.send_keys(FB_USERNAME)
    # tinder_continue_button = driver.find_element(By.CSS_SELECTOR, '[class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Ell Bdrs(100px) Px(24px) Px(20px)--s Py(0) Mih(54px) Pos(r) Ov(h) C(#fff) Bg($c-pink):h::b Bg($c-pink):f::b Bg($c-pink):a::b Trsdu($fast) Trsp($background) Bg($g-ds-background-brand-gradient) button--primary-shadow StyledButton Bxsh($bxsh-btn) Fw($semibold) focus-button-style My(20px) My(12px)--xs Maw(315px) W(100%) Ell"]')
    # tinder_continue_button.click()

    # if input("Type 'y' to continue and 'n' to end: ").lower() == "y":
    #     print("continue")
    #     tinder_phone_number_input = driver.find_element(By.CSS_SELECTOR,
    #                                                     '[class="Fz($m) Va(m) Py(8px) Bdrs(4px)--ml Bgc($c-divider-lite)--ml Px(8px)--ml BdB--s Bdrs(0)--s Bdbc($c-secondary)--s Px(4px)--s D(ib) Lts($ls-m) Bdrsbstart(0)! Bdrststart(0)!"]')
    #     tinder_phone_number_input.send_keys(FB_USERNAME)
    #     tinder_continue_button = driver.find_element(By.CSS_SELECTOR,
    #                                                  '[class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Ell Bdrs(100px) Px(24px) Px(20px)--s Py(0) Mih(54px) Pos(r) Ov(h) C(#fff) Bg($c-pink):h::b Bg($c-pink):f::b Bg($c-pink):a::b Trsdu($fast) Trsp($background) Bg($g-ds-background-brand-gradient) button--primary-shadow StyledButton Bxsh($bxsh-btn) Fw($semibold) focus-button-style My(20px) My(12px)--xs Maw(315px) W(100%) Ell"]')
    #     tinder_continue_button.click()
    # else:
    #     print("end")
    try:
        use_location_allow_button = driver.find_element(By.CSS_SELECTOR,
                                                        '[class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Ell Bdrs(100px) Px(24px) Px(20px)--s Py(0) Mih(40px) Pos(r) Ov(h) C(#fff) Bg($c-pink):h::b Bg($c-pink):f::b Bg($c-pink):a::b Trsdu($fast) Trsp($background) Bg($g-ds-background-brand-gradient) button--primary-shadow StyledButton Bxsh($bxsh-btn) Fw($semibold) focus-button-style W(225px) W(a) Mstart(8px)"]')
    except selenium.common.exceptions.NoSuchElementException:
        print("It appears that FaceBook Login has timed out due to excessive recent logins. Exiting program.")
    else:
        use_location_allow_button.click()
        get_notifications_enable_button = driver.find_element(By.CSS_SELECTOR,
                                                                  '[class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Ell Bdrs(100px) Px(24px) Px(20px)--s Py(0) Mih(40px) Pos(r) Ov(h) C(#fff) Bg($c-pink):h::b Bg($c-pink):f::b Bg($c-pink):a::b Trsdu($fast) Trsp($background) Bg($g-ds-background-brand-gradient) button--primary-shadow StyledButton Bxsh($bxsh-btn) Fw($semibold) focus-button-style W(225px) W(a) Mstart(8px)"]')
        get_notifications_enable_button.click()
        allow_cookies_button = driver.find_element(By.CSS_SELECTOR,
                                                       '[class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Ell Bdrs(100px) Px(24px) Px(20px)--s Py(0) Mih(40px) button--outline Bdw(2px) Bds(s) Trsdu($fast) Bdc($c-ds-border-button-secondary) C($c-ds-foreground-button-secondary) Bdc($c-ds-border-button-secondary):h C($c-base):h Bdc($c-ds-border-button-secondary):f C($c-base):f Bdc($c-ds-border-button-secondary):a C($c-base):a Fw($semibold) focus-button-style W(100%) W(a)--ml Mx(4px)--ml My(0)--ml"]')
        allow_cookies_button.click()
        time.sleep(5)


def click_like_button():
    like_button = driver.find_element(By.CSS_SELECTOR,
                                      '[class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Bdrs(50%) P(0) Fw($semibold) focus-button-style Bxsh($bxsh-btn) Expand Trstf(e) Trsdu($normal) Wc($transform) Pe(a) Scale(1.1):h Scale(.9):a Bgc($c-like-green):a"]')
    like_button.click()


def swipe_right(i):
    # limit = input("How many people would you like to 'like'? ")
    #
    # while not limit.isnumeric():
    #     limit = input("How many people would you like to 'like'? ")
    #
    # limit = int(limit)
    proceed = True
    #
    # while i < limit:
    try:
        click_like_button()
    except selenium.common.exceptions.NoSuchElementException:  # page is slow to load
        time.sleep(3)
        # click_like_button()
    except selenium.common.exceptions.ElementClickInterceptedException:  # 'you have a match' notification appears
        try:
            dismiss_button = driver.find_element(By.XPATH, '//*[@id="o615757898"]/div/div/div[1]/div/div[3]/button')
            dismiss_button.click()
        except selenium.common.exceptions.NoSuchElementException:  # 'add to homepage' notificatiom appears
            try:
                dismiss_button_2 = driver.find_element(By.CSS_SELECTOR,
                                                       '[class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Ell Bdrs(100px) Px(24px) Px(20px)--s Py(0) Mih(42px)--s Mih(50px)--ml C($c-secondary) C($c-base):h Fw($semibold) focus-button-style D(b) Mx(a)"]')
                dismiss_button_2.click()
            except selenium.common.exceptions.NoSuchElementException:  # out of likes notification appears
                if input("You are out of likes; type 'y' to keep clicking. ").lower() == "y":
                    dismiss_button_3 = driver.find_element(By.CSS_SELECTOR,
                                                           '[class="button Lts($ls-s) Z(0) CenterAlign Mx(a) Cur(p) Tt(u) Ell Bdrs(100px) Px(24px) Px(20px)--s Py(0) Mih(40px) C($c-secondary) C($c-base):h Fw($semibold) focus-button-style D(b) Mx(a)"]')
                    dismiss_button_3.click()
                else:
                    proceed = False
    else:
        i = i + 1
        print(f"'{i}' people liked.")
    if proceed:
        swipe_right(i)
    # else:


def check_messages():
    messages_button = driver.find_element(By.CSS_SELECTOR, '[class="Mstart(16px) D(ib) Va(m)"]')
    messages_button.click()
    matches = driver.find_elements(By.CSS_SELECTOR, '[class="D(ib) Fxg(0) Px(12px) Py(8px) Px(20px)--m Px(24px)--l Py(12px)--ml M(-1px)--s BdB--s Bdc(#fff)--s"]')
    for match in matches:
        match.click()


def choose_action():
    action = input(
        "Please enter ONE of the following actions for the program to perform: 'exhaust swipes','check messages', 'send messages', 'collect analytics' ").lower()
    print(action)
    actions = ['exhaust swipes', 'check messages', 'send messages', 'collect analytics']
    while action not in actions:
        action = input(f"The action you entered was not found. Please enter ONE of the following actions: {actions}")
    return action

setup_tinder()
action = choose_action()
if action == "exhaust swipes":
    swipe_right(i=0)
elif action == "check messages":
    print("checking messages")
    check_messages()
