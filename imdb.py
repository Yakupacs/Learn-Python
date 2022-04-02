import requests
from bs4 import BeautifulSoup
url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")

list = soup.find("tbody", {"class":"lister-list"}).find_all("tr")
print("IMDB TOP 250 MOVIES")
i = 1
for tr in list:
    title = tr.find("td",{"class":"titleColumn"}).find("a").text
    rating = tr.find("td",{"class":"ratingColumn imdbRating"}).find("strong").text
    year = tr.find("td",{"class":"titleColumn"}).find("span").text.strip("()")
    print(f"{i}. {title.ljust(50)}  Year: {year}, Rating: {rating}")
    i = i + 1