from bs4 import BeautifulSoup
from pprint import pprint
import lxml  # provides a parser that may be necessary for some websites
import requests
import os
import time
from selenium import webdriver
import codecs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


GOOGLE_FORMS_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSda7n2DDy1_JoGvnKLnq87Ow0s9SMofMxou_OvPXVg-nsnyTw/viewform?usp=sf_link"
ZILLOW_LINK = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-122.69425429296875%2C%22east%22%3A-122.17240370703125%2C%22south%22%3A37.54699039150629%2C%22north%22%3A38.0028896874157%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"

ITEMS = {}

# for some reason, any requests to the Zillow page failed (or, at least, Beautiful Soup failed to scan them)
# thus, I decided to save the webpage to the local folder
def save_webpage():
    # webdriver
    chrome_driver_path = r"C:\Users\nthne\OneDrive\OneDrive-UW\UW-OneDrive\Documents\100 Days of Python\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)


    driver.implicitly_wait(0.5)

    # maximize browser
    driver.maximize_window()

    # launch URL
    driver.get(ZILLOW_LINK)
    # wait 5 seconds to allow the webpage to load completely
    time.sleep(5)

    # get file path to save page
    n = os.path.join(r"C:\Users\nthne\OneDrive\OneDrive-UW\UW-OneDrive\Documents\100 Days of Python\Day 54\\",
                     "ZillowWebPage.html")
    # open file in write mode with encoding
    f = codecs.open(n, "w", "utf−8")
    # obtain page source
    h = driver.page_source
    # write page source content to file
    f.write(h)
    # close browser
    #driver.quit()

# this function parses the zillow page and
# adds to a dictionary "ITEMS" entries from the page,
# including a list of prices, a list of addresses, and a list of links
def parse_page():

    path = r"Rental Listings - 800 Rentals _ Zillow.html"
    with open(path, encoding="utf8") as file:
        contents = file.read()
    soup = BeautifulSoup(contents, "html.parser")

    global ITEMS

    prices = soup.find_all(name="div", class_="list-card-price")
    addresses = soup.find_all(name="address", class_="list-card-addr")
    links = soup.find_all(name="a", class_="list-card-link")


    # since a standard parsing of the page for "a" tags with class "list-card-link"
    # produces with two occurrences of each link, this algorithm removes the second
    # of each link
    # integer division provides the correct stop value for lists of odd length, e.g., 9/2 = 4 and 7/2 = 3.
    for i in range(1, int(len(links)/2), 1):
        links.pop(i)

    # for address in addresses:
    #     print(address)
    #
    # for price in prices:
    #     print(price)
    #
    # for link in links:
    #     print(link)
    # print(addresses[0])
    # print(prices[0])
    # print(links[0])
    for i in range(0, len(addresses)):
        address = addresses[i]
        price = prices[i]
        link = links[i]
        ITEMS[address.text] = {"price": price.text, "link": link["href"]}
        # print(address)
        # print(price)
        # print(link)
        #ITEMS[address] = {price, link}
    for item in ITEMS.keys():
        print(item)
        print(ITEMS[item])
    # code for testing purposes
    # #print(items["addresses"])
    # print("Addresses Length")
    # print(len(ITEMS["addresses"]))
    # print("Prices Length")
    # print(len(ITEMS["prices"]))
    # print("Links Length")
    # print(len(ITEMS["links"]))
    # print()
    # for i in range(0, len(ITEMS["addresses"])):
    #     print("Address:")
    #     print(ITEMS["addresses"][i].text)
    #     print("Price:")
    #     print(ITEMS["prices"][i].text)
    #     print("Link:")
    #     print(ITEMS["links"][i]["href"])


def post_to_form():
    chrome_driver_path = r"C:\Users\nthne\OneDrive\OneDrive-UW\UW-OneDrive\Documents\100 Days of Python\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.get(GOOGLE_FORMS_LINK)
    # address_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # price_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # link_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    for item in ITEMS.keys():
        address_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        address_field.send_keys(item)
        price_field.send_keys(ITEMS[item]["price"])
        link_field.send_keys(ITEMS[item]["link"])
        #if input("Would you like to submit? y/n ").lower() == "y":
        submit_button.click()
        time.sleep(1)
        submit_again_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")
        submit_again_button.click()
        time.sleep(1)


    if input("Would you like to exit? y/n ").lower() == "y":
        driver.quit()
    #https://docs.google.com/forms/d/e/1FAIpQLSda7n2DDy1_JoGvnKLnq87Ow0s9SMofMxou_OvPXVg-nsnyTw/viewform?usp=sf_link





#save_webpage()
parse_page()
post_to_form()




