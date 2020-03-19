import requests
from bs4 import BeautifulSoup
url="https://www.boxofficemojo.com/weekend/by-year/2019/"
page_text=requests.get(url).text

soup= BeautifulSoup(page_text, "html.parser")

print(soup.prettify())

