import requests

from bs4 import BeautifulSoup

adres = "http://trojmiasto.pl"

response = requests.get(adres)

print(response.status_code)

response.raise_for_status()

print()

class S():
    def __init__(self,marka,kolor):
        self.producent = marka
        self.kolor = kolor

auto =S("volvo","czarny")
auto.model = "Xc"
print(auto.model)