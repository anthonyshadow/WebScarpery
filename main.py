from bs4 import BeautifulSoup
import requests


# Scrapes the requested webpage for your term and then gives you data properly organized usiing beautifulsoup


# search = input("Enter Search Term: ")
# params = {"q": search}
# r = requests.get("https://www.bing.com/search", params=params)

# soup = BeautifulSoup(r.text)
# print(soup.prettify())


# ---------------------------------------------------------------------------------------------


# Parsing our soup, prints the link name and the link itself

search = input("Search for: ")
params = {"q": search}
r = requests.get("https://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text, "html.parser")

results = soup.find("ol", {"id": "b_results"})
links = results.findAll("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_href = item.find("a").attrs["href"]

    if item_text and item_href:
        print(item_text)
        print(item_href)
        # Navigating items through parents and children of item
        print("Summary:", item.find("a").parent.parent.find("p").text)

        # All children

        # children = item.children
        # for child in children:
        #     print("Child", child)

        # Sibling

        children = item.find("h2")
        #can do previous sibling instead of next if you want to go up
        print("Next Sibling of the h2:", children.next_sibling)



