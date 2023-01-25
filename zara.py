import requests
from bs4 import BeautifulSoup
from requests.exceptions import ConnectionError


class Zara:
    headers = {
        'User-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0'}
    URLS = []

    def __init__(self, URL):

        self.URL = URL
        self.html_page = self.get_html()
        self.name = self.get_name()
        self.price = self.get_price()
        self.is_stock = False
        self.URLS.append(self)
        self.stock_control()
        
        
    def get_html(self):
        try:
            response = requests.get(self.URL, headers=Zara.headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup
        except ConnectionError:
            return False

    def stock_control(self):
        if self.html_page:
            buttons = self.html_page.find(class_="zds-button")
            if buttons.text == "TÜKENDİ":
                self.is_stock = False   
            else:
                self.is_stock = True
                    

    def get_name(self):
        if self.html_page:
            header = self.html_page.find(class_="product-detail-info__header-name").text
            return header

    def get_price(self):
        if self.html_page:
            current_price_text = self.html_page.find(class_="price-current__amount").text
            current_price = current_price_text.split(' ')[0]
            
            return current_price.replace(",",".")
