from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = r"C:\Users\nthne\OneDrive\OneDrive-UW\UW-OneDrive\Documents\100 Days of Python\chromedriver.exe"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
#price = driver.find_element(By.CLASS_NAME, "a-offscreen")
#text = driver.find_element_by_id("a-price-whole")
#print(price.text)
# search_box = driver.find_element(By.NAME, "q")
# jobs_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
# element = driver.find_element(By.XPATH, '//*[@id="container"]/li[1]/ul/li[3]/a')
events_element = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')
print(type(events_element.text))

event_list = [events_element.text.split("\n")][0]
events = {f"{int(i/2)}": {"time": event_list[i], "name": event_list[i+1]}
          for i in range(0, len(event_list)) if i % 2 == 0}
#print(events)

# events = {event_list[i]: event_list[i+1] for i in range(0, len(event_list), 2)
# print(events)
# list_1 = [1, 2, 3]
#
# #print(len(event_list))
#
# print(event_list[0])

# events = {}
# #
# for i in range(0, len(event_list), 2):
#     events[i] = {event_list[i]: event_list[i+1]}
#
# print(events)

#print(len(event_list))

# for i in range(0, len(event_list), 2):
#     print(i)

# for i in event_list[0:len(event_list):2]:
#     print(i)







#driver.close()  # closes the tab

driver.quit() #closes the entire browser

