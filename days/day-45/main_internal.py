from bs4 import BeautifulSoup

with open("days/day-45/website.html") as file:
    contens = file.read()  # read the website.htlm content

soup = BeautifulSoup(contens, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.prettify())

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     print(tag.getText())


# get all links!
# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     print(tag.get("href"))

# all_anchor_tags = soup.find_all(name="a")

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)
