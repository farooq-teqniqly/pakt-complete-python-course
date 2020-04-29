from bs4 import BeautifulSoup
from stringcase import snakecase

with open("simple.html", "r") as reader:
    html_text = reader.read()

soup = BeautifulSoup(html_text, "html.parser")

p_tags = soup.find_all("p")

print(p_tags)
print(p_tags[1].string)

link_text = [link.string.strip() for link in soup.find_all("a")]
print(link_text)

link_dict = {snakecase(link.string.lower()): link["href"] for link in soup.select("li a") if link.attrs.get("href")}
print(link_dict)

page_title = (soup.select("head > title")[0]).string
print(page_title)

print(soup.select("h1"))

h1_by_class = (soup.select("h1.heading2")[0]).string
print(h1_by_class)

link_tags_without_href = [link for link in soup.find_all("a") if not link.attrs.get("href")]
print(link_tags_without_href)