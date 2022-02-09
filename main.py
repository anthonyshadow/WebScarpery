from bs4 import BeautifulSoup
import requests


# Scrapes the requested webpage for your term and then gives you data properly organized
search = input("Enter Search Term: ")
params = {"q": search}
r = requests.get("https://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text)
print(soup.prettify())