import requests
from bs4 import BeautifulSoup

t_price = 50

def scrape(*urls):
        for url in urls:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, "html.parser")

            # get title
            title = soup.h1.string

            # get price
            price = soup.find("p", class_="price_color").text
            price = float(price[2:])

            # get img rel path
            img_container = soup.find("div", class_="item active")
            img_src = img_container.find("img")["src"]

            # remove everything before media/
            img_url = "https://books.toscrape.com/" + img_src[5:]

            # title, price, img
            c_price = int(t_price-price)
            print(f"Title: {title}")
            print(f"Price: {price}")
            print(f"Image URL: {img_url}")
            print(f'comparison with target price:{c_price}')

            # dwnld img
            img_response = requests.get(img_url)

            # clean name
            clean_name = img_url.split("/")[-1]

            # save
            with open(clean_name, "wb") as f:
                f.write(img_response.content)

            print(f"Saved image successfully as: {clean_name}")

scrape("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html","https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html")
