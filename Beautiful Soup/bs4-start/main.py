from bs4 import BeautifulSoup
import lxml
with open("website.html") as file:
  contents = file.read()


soup = BeautifulSoup(contents,"html.parser")
print(soup.title)
print(soup.title.string)

#complete html code
print(soup.prettify())

#give first anchor
print(soup.a)

#give first p tag
print(soup.p)

all_anchor_tags=soup.findall(name="a")

for tag in all_anchor_tags:
  print(tag.getText())
  print(tag.get("href"))

heading= soup.find(name="h1", id = "name")
print(heading)
section_heading= soup.find(name="h1", class_ = "heading")

print(section_heading.get("class"))

#a tag in a p tag
company_url = soup.select_one(selector="p a")

# to get the id element
company_url = soup.select_one(selector="#name")

# to get the all class element
company_url = soup.select(selector=".heading")