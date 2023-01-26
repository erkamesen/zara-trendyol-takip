import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError


class Shop:
    headers = {
        'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0'}
    stock_list = []
    discount_list = []

    def __init__(self, URL, price_check=False):

        self.URL = URL
        self.price_check = price_check
        self.html_page = self.get_html()
        self.name = self.get_name()
        self.price = self.get_price()
        self.is_stock = False
        self.stock_price_control()

    def get_html(self):
        try:
            response = requests.get(self.URL, headers=Shop.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
        except ConnectionError:
            return False

    def stock_price_control(self):
        if self.price_check:
            Shop.discount_list.append(self)
        else:
            if self.html_page:
                if "www.trendyol.com" in self.URL:
                    button = self.html_page.find(class_="sold-out")
                    if button:
                        self.is_stock = False
                        Shop.stock_list.append(self)
                    else:
                        Shop.stock_list.append(self)
                        self.is_stock = True

                else:
                    buttons = self.html_page.find(class_="zds-button")
                    if buttons.text == "TÜKENDİ":
                        self.is_stock = False
                        Shop.stock_list.append(self)
                    else:
                        Shop.stock_list.append(self)
                        self.is_stock = True

    def get_name(self):
        if self.html_page:
            if "www.trendyol.com" in self.URL:
                name = self.html_page.find(class_="pr-new-br")
                return name.span.text.strip()
            else:
                header = self.html_page.find(
                    class_="product-detail-info__header-name").text
                return header

    def get_price(self):
        if self.html_page:
            if "www.trendyol.com" in self.URL:
                price = self.html_page.find(class_="prc-dsc")
                return price.text.split(" ")[0].replace(",", ".")
            else:
                current_price_text = self.html_page.find(
                    class_="price-current__amount").text
                current_price = current_price_text.split(' ')[0]

                return current_price.replace(",", ".")
