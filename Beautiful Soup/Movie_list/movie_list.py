import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text
print(website_html)
soup=BeautifulSoup(website_html,"html_parser")
all_movies=soup.findall(name="a", class_="meta-title")
movie_title = [movie.getText() for movie in all_movies]

with open("movies.txt",mode ="w") as file:
  for movie in movie_title:
    file.write(f"{movie}\n")

    
