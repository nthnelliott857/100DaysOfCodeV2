from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = r"C:\Users\nthne\OneDrive\OneDrive-UW\UW-OneDrive\Documents\100 Days of Python\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
#
# article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# #article_count.click()
# #print(article_count.text)
# all_portals = driver.find_element(By.LINK_TEXT, "Content portals")
# #all_portals.click()
#
# search = driver.find_element(By.NAME, "search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)


driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, "fName")
last_name = driver.find_element(By.NAME, "lName")
email = driver.find_element(By.NAME, "email")
sign_up = driver.find_element(By.CSS_SELECTOR, '[class="btn btn-lg btn-primary btn-block"]')

first_name.send_keys("Vladmir")
last_name.send_keys("Putin")
email.send_keys("vp@kremlin.ru")
sign_up.click()




#driver.quit()