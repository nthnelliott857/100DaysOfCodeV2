import os
from selenium import webdriver
import codecs


driver = webdriver.Chrome(executable_path=r"C:\Users\nthne\Downloads\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(0.5)

#maximize browser
driver.maximize_window()

#launch URL
driver.get("https://www.tutorialspoint.com/index.htm")

#get file path to save page
n = os.path.join(r"C:\Users\nthne\Downloads\\", "Page.html")
#open file in write mode with encoding
f = codecs.open(n, "w", "utf−8")
#obtain page source
h = driver.page_source
#write page source content to file
f.write(h)
#close browser
driver.quit()
