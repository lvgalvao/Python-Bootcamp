from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

if response.status_code == 200:
    yc_web_page = response.text

    soup = BeautifulSoup(yc_web_page, "html.parser")
    article_tag = soup.find(name="span", class_="titleline")
    article_text = article_tag.getText()

    print(article_text)
