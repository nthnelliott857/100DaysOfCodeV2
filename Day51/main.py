import json

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from internetspeedtwitterbot import InternetSpeedTwitterBot

PROMISED_DOWN = 100
PROMISED_UP = 10



twitter_bot = InternetSpeedTwitterBot()
twitter_bot.get_internet_speed()
twitter_bot.tweet_at_provider()

