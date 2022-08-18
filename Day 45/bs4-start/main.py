from bs4 import BeautifulSoup
import lxml  # provides a parser that may be necessary for some websites
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.get_text()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts)
# print(article_links)
print(article_upvotes)
#print(article_upvotes[0].split(" "))

# article_upvotes = [int(score.split(" ")[0]) for score in article_upvotes]
print(max(article_upvotes))
# print(article_tag.get_text())
# article_link = article_tag.get("href")
# print(article_link)
# article_upvotes = soup.find(name="span", class_="score")
# print(article_upvotes.get_text())












# with open("website.html", encoding="utf8") as file:
#     contents = file.read()
#
# # soup = BeautifulSoup(markup=contents, parser="html.parser")
# soup = BeautifulSoup(contents, "html.parser")
#
# # print(soup.title.string)
# all_anchor_tags = soup.find_all(name="a")
# #print(all_anchor_tags)
#
# tags = [tag.get("href") for tag in all_anchor_tags]
# #print(tags)
#
#
# heading = soup.find(name="h1", id="name") # only prints the h1 attribute with a id of "name"
#
# # section_heading = soup.find(name="h3", class_="heading")
# # print(section_heading)
# # #print(heading)
# #
# # company_url = soup.select_one(selector="p a")
# # print(company_url)
# #
# # name = soup.select_one(selector="#name")
# # print(name)
# #
# # headings = soup.select(selector=".heading")
# # print(headings)
#
# headings1 = soup.select("li a")
# headings2 = soup.select("a, li")
# print(headings1)
# print(headings2)
