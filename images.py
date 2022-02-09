from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO

# Saving Images from bing based on search

search = input("Search For: ")
params = {"q": search}
r = requests.get("http://www.bing.com/images/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")
links = soup.findAll("a", {"class": "thumb"})

for item in links:
    img_obj = requests.get(item.attrs["href"])
    print("Getting", item.attrs["href"])
    # To get the last in a list in python use -1
    title = item.attrs["href"].split("/")[-1]
    img = Image.open(BytesIO(img_obj.content))

    # Saves scraped images to new directory
    path = "./scraped_images/"
    img.save(path + title, img.format)


