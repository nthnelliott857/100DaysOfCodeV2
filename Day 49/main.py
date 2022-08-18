import json

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait

USERNAME = os.environ["LinkedIn Username"]
PASSWORD = os.environ["LinkedIn Password"]
EMAIL = os.environ["email"]
PHONE_NUMBER = os.environ["phone_number"]

with open("data.json", mode="r", encoding="utf8") as file:
    DATA = json.load(file)
print(DATA)

chrome_driver_path = r"C:\Users\nthne\OneDrive\OneDrive-UW\UW-OneDrive\Documents\100 Days of Python\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3072620203&f_AL=true")
sign_in = driver.find_element(By.CLASS_NAME, "nav__button-secondary")
sign_in.click()
time.sleep(1)
username_field = driver.find_element(By.NAME, "session_key")
password_field = driver.find_element(By.NAME, "session_password")

sign_in_2 = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
username_field.send_keys(USERNAME)
password_field.send_keys(PASSWORD)
sign_in_2.click()

# collects the job elements from the job feed
job_elements = driver.find_elements(By.CSS_SELECTOR,
                                    '[class="disabled ember-view job-card-container__link job-card-list__title"]')

# print([job.text for job in job_elements])

# for job in job_elements:
#     link = driver.find_element(By.LINK_TEXT, job.text)
#     link.click()
#     time.sleep(1)
#     print(link.text)

# iterates through the job elements
for job in job_elements:
    link = driver.find_element(By.LINK_TEXT,
                               job.text)  # find the job element by its link name, e.g., "Data I/O Technician"
    link.click()  # clicks job element
    time.sleep(1)  # waits 1 second for easy apply button to appear
    easy_apply = driver.find_element(By.CSS_SELECTOR,
                                     '[class="jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view"]')  # collects easy apply button
    easy_apply.click()  # clicks easy apply button
    # at this point, the application is asking for a name, email address, and phone number, all of which are auto-filled, so the application just needs to be moved to the next step
    next_button = driver.find_element(By.CSS_SELECTOR, '[class="artdeco-button artdeco-button--2 '
                                                       'artdeco-button--primary ember-view"]')
    next_button.click()  # clicks the "next button", which proceeds to the "resume" page
    next_button.click()  # proceeds past the "resume" page
    further_questions = driver.find_elements(By.CSS_SELECTOR, '[class="pb4"]')
    questions = [further_question.text.split("\n") for further_question in further_questions].pop(0)

    # at this point, it's pretty difficult to anticipate the questions that each form will ask without some form of
    # natural language processing. I was trying to do it by building a JSON file containing previously-answered
    # questions in it, but that approach was bound to run into problems. However, I am able to apply to basic easy
    # apply applications without too much trouble. It's another matter, however, finding the applications to which
    # you can submit an application in one step because just about every one of them requires that you answer further
    # questions.

    for i in range(1, len(questions)):
        if questions[i].endswith("?"):
            item = questions[i]
            if item[i + 2] == "Yes":
                item_type = "radio"
            else:
                item_type = "text"
            if item not in DATA:
                DATA[item] = {
                    "type": item_type,
                    "value": input(f"{item} type: {item_type}")
                }
    with open("data.json", mode="w") as file:
        json.dump(DATA, file, indent=4)
        # field = driver.find_element(By.LINK_TEXT, f"{item}")
        # field.send_keys(DATA[item]["value"])

    # for further_question in further_questions:
    #     print(f"Type: {further_question.get_property(name='class')}")
    #     print(f"Value: {further_question.text}")
    #     if further_question.text in DATA:
    #         print(f"Answer: {DATA[further_question.text]}")
    # if further_question.text in DATA:
    #
    #
    # else:
    #     new_answer = input(f"{further_question.text} ")
    #     DATA[further_question.text] = {
    #         "type": further_question.ty
    #     }

#     print([further_question.text for further_question in further_questions])
# try:
#     driver.find_element(By.CSS_SELECTOR, '[class="artdeco-button artdeco-button--2 artdeco-button--primary ember-view"]')
# except selenium.common.exceptions.InvalidSelectorException:
#     back_button = driver.find_element(By.CSS_SELECTOR, '[class="artdeco-modal__dismiss artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view"]')
# else:
#     phone_number = driver.find_element(By.NAME, 'urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3067332981,9,phoneNumber~nationalNumber)')
#     phone_number.send_keys(PHONE_NUMBER)
#     next_button_1 = driver.find_element(By.CSS_SELECTOR, '[class="artdeco-button artdeco-button--2 artdeco-button--primary ember-view"]')
#     next_button_1.click()


# easy_apply_link = '[class="jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view"]'
#
# #WebDriverWait(driver=driver, timeout=1).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, easy_apply_xpath)))
# easy_apply = driver.find_element(By.CSS_SELECTOR, easy_apply_link)
# easy_apply.click()
# phone_number = driver.find_element(By.NAME, 'urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:3067332981,9,phoneNumber~nationalNumber)')
# phone_number.send_keys(PHONE_NUMBER)
# next_button_1 = driver.find_element(By.CSS_SELECTOR, '[class="artdeco-button artdeco-button--2 artdeco-button--primary ember-view"]')
# next_button_1.click()
# time.sleep(1)
# next_button_1.click()
# next_button_2 = driver.find_element(By.CSS_SELECTOR, '[class="mr2 artdeco-button artdeco-button--2 artdeco-button--tertiary ember-view"]')
# next_button_2.click()
# print(sign_in.text)
# driver.quit()
# cookie = driver.find_element(By.ID, "cookie")
