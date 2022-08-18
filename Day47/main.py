import os
from selenium import webdriver
import codecs
import requests
from bs4 import BeautifulSoup
import lxml
import datetime as dt
import smtplib

# PRODUCT_TO_SCRAPE = "https://www.amazon.com/Trijicon-Illuminated-Chevron-Rifle-Combat/dp/B0010PR0QG/"
# PRODUCT_TO_SCRAPE = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463&th=1"
PRODUCT_URL = "https://www.amazon.com/Green-Mountain-Grills-Crockett-Controlled/dp/B078RXH95C/ref=sr_1_1_sspa?" \
                    "crid=4RYUNZEI9XZW&keywords=green+mountain+smoker&qid=1650756128&sprefix=green+mountain+smoke%2" \
                    "Caps%2C186&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEySFhEVFdaQ1E5VTAmZW5jcnlwdGVkSWQ9" \
                    "QTA1OTg1NjYxNEtJNjNaNjVHSlFWJmVuY3J5cHRlZEFkSWQ9QTA3NTM1NjQxQzM5N0c0REsxRlFUJndpZGdldE5hbWU9c3Bf" \
                    "YXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=="
PRODUCT_NAME = PRODUCT_URL.split("/")[3]
FILE_NAME = PRODUCT_NAME + " " + str(dt.datetime.now().date()) + ".html"
PRODUCT_PRICE = None
ALERT_PRICE = 20000.00
PRODUCT_PRICE_LESS_THAN_ALERT_PRICE = False


# print(FILE_NAME)

def save_webpage():
    # webdriver

    driver = webdriver.Chrome(executable_path=r"C:\Users\nthne\Downloads\chromedriver_win32\chromedriver.exe")
    driver.implicitly_wait(0.5)

    # maximize browser
    driver.maximize_window()

    # launch URL
    driver.get(PRODUCT_URL)

    # get file path to save page
    n = os.path.join(r"C:\Users\nthne\OneDrive\OneDrive-UW\UW-OneDrive\Documents\100 Days of Python\Day47\\",
                     FILE_NAME)
    # open file in write mode with encoding
    f = codecs.open(n, "w", "utf−8")
    # obtain page source
    h = driver.page_source
    # write page source content to file
    f.write(h)
    # close browser
    driver.quit()


def parse_page():
    path = r"C:\Users\nthne\OneDrive\OneDrive-UW\UW-OneDrive\Documents\100 Days of Python\Day47\\"
    path = path + FILE_NAME
    try:
        open(path, encoding="utf8")
        # print(contents)
    except FileNotFoundError:
        print("Error: specified file does not exist.")
    else:
        with open(path, encoding="utf8") as file:
            contents = file.read()
        soup = BeautifulSoup(contents, "html.parser")
        item_name = soup.find(name="span", class_="a-size-large product-title-word-break")
        whole_price = float("".join(soup.find(name="span", class_="a-price-whole").text.split(".")[0].split(",")))
        decimal_price = float("0." + soup.find(name="span", class_="a-price-fraction").text)
        global PRODUCT_PRICE
        PRODUCT_PRICE = whole_price + decimal_price
        global ALERT_PRICE
        if PRODUCT_PRICE < ALERT_PRICE:
            global PRODUCT_PRICE_LESS_THAN_ALERT_PRICE
            PRODUCT_PRICE_LESS_THAN_ALERT_PRICE = True


        # print(whole_price + decimal_price)
        # whole_price = format(whole_price, ".2f")
        # whole_price = [for char in whole_price]
        # print(whole_price)
        # print(decimal_price)
        # whole_price = int(whole_price)

        # print(soup)
        print(f"{PRODUCT_NAME}: ${whole_price + decimal_price}")


def send_notification_email():
    my_email = "natedoggg109312@gmail.com"
    my_password = "HorseDartNinjaPilot#6"
    message = "Subject: Low Price Alert\n"
    message += f"{PRODUCT_NAME} is only ${PRODUCT_PRICE}, which is below the alert price of ${ALERT_PRICE}."

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs="nthnelliott857@gmail.com", msg=message)


# Execution
save_webpage()
parse_page()
if PRODUCT_PRICE_LESS_THAN_ALERT_PRICE:
    send_notification_email()







# s = "1,089"
# j = s.split(",")
# s = "".join(j)
#
# print(s)
