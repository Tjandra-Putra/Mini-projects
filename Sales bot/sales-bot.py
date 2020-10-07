from bs4 import BeautifulSoup
import requests
from twilio.rest import Client

# Twilio configuration
client = Client("<account_sid>", "<auth_token>")
from_whats_app_number = "whatsapp:+1xxxxxxxxxx"
to_whats_app_number = "whatsapp:+65xxxxxxxx"


# Web scraping
source = requests.get("https://www.newegg.com/global/sg-en/p/pl?d=graphic+card").text

soup = BeautifulSoup(source, 'html')

item_container = soup.findAll("div", {"class": "item-container"})

for item in item_container:
    brand = item.find("a", class_="item-brand").img['title']
    title = item.a.img["title"]
    price = item.find('li', 'price-current').strong.text

    if float(price.replace(',', '.')) <= 200 and brand == "MSI":
        print("-------------------------------")
        print("BRAND: " + brand)
        print("TITLE: " + title)
        print("PRICE: $" + str(price))

        client.messages.create(body="'{}' is on sale! Price: $ {}".format(title, str(price)),
                               from_=from_whats_app_number,
                               to=to_whats_app_number)

