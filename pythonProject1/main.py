import requests
from bs4 import BeautifulSoup
import lxml
import scrapy

# HEADERS = {
#     "Accept": "gzip, deflate",
#     "Accept-Encoding": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44",
#     "Accept-Language": "en-US,en;q=0.9",
#     "Connection": "keep-alive",
# }

response = requests.get(
    f"https://www.opticsplanet.com/trijicon-acog-4x32-scope-kit-green-chevron-bac-flattop-reticle-ta51-mount.html")
amazon_webpage = response.text
print(amazon_webpage)

