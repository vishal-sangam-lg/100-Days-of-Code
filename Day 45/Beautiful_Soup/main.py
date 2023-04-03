# www.example.com/robots.txt -> Details on what not to scrape

from bs4 import BeautifulSoup

with open("website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
# # Explore Beautiful Soup
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())

# print(soup.li)
# print(soup.findAll(name="a"))
# print(soup.findAll(name="p"))

# all_anchor_tags = soup.findAll(name="a")
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

# # Selecting Elements
# heading = soup.find(name="h1", id="name")
# print(heading)
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
# company_url = soup.select_one(selector="p a")
# print(company_url)
# headings = soup.select(".heading")
# print(headings)
