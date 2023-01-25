import requests
from bs4 import BeautifulSoup
from telegram import Logger
from zara import Zara
from dotenv import load_dotenv
import os

load_dotenv()


## TELEGRAM API KEY VE CHATID GİR
# 2 ADET HESABA ATTIĞIM İÇİN 2 ADET LOGGER KULLANDIM
logger = Logger(
    token=os.getenv("APIKey"), chat_id=os.getenv('chatID1'))
logger2 = Logger(
    token=os.getenv("APIKey"), chat_id=os.getenv("chatID2"))


""" STOK TAKİBİ """

stock_URL1 = "https://www.zara.com/tr/tr/share/-p04387241.html?utm_campaign=productMultiShare&utm_medium=mobile_sharing_iOS&utm_source=red_social_movil&v1=223811112"
stock_URL2 = "https://www.zara.com/tr/tr/share/-p01255896.html?utm_campaign=productMultiShare&utm_medium=mobile_sharing_iOS&utm_source=red_social_movil&v1=224850511"
stock_URL3 = "https://www.zara.com/tr/tr/share/-p01255825.html?utm_campaign=productMultiShare&utm_medium=mobile_sharing_iOS&utm_source=red_social_movil&v1=186613774"
stock_URL4 = "https://www.zara.com/tr/tr/share/-p05854714.html?utm_campaign=productMultiShare&utm_medium=mobile_sharing_iOS&utm_source=red_social_movil&v1=178078856"
stock_URL5 = "https://www.zara.com/tr/tr/share/-p03046274.html?utm_campaign=productMultiShare&utm_medium=mobile_sharing_iOS&utm_source=red_social_movil&v1=223692936"
stock_URL6 = "https://www.zara.com/tr/tr/share/-p03046313.html?utm_campaign=productMultiShare &utm_medium=mobile_sharing_iOS&utm_source=red_social_movil&v1=188530143"



stock1 = Zara(stock_URL1)
stock2 = Zara(stock_URL2)
stock3 = Zara(stock_URL3)
stock4 = Zara(stock_URL4)
stock5 = Zara(stock_URL5)
stock6 = Zara(stock_URL6)



def stock_message(url, name, price):
    return f"Stoğa Girdi !!!!\n********************\nÜrün Adı: {name}\nGüncel Fiyat: {price} TL\n********************\n{url}"


for product in Zara.URLS:
    if product.is_stock:
        stock_msg = stock_message(url=product.URL,
                                  name=product.name,
                                  price=product.price
                                  )
        logger.info(message=stock_msg)
        logger2.info(message=stock_msg)


""" FİYAT TAKİBİ """

price_URL1 = "https://www.zara.com/tr/tr/zw-90-s-wide-leg-suni-deri-pantolon-p02969242.html"
price1 = 659.95
price_URL2 = "https://www.zara.com/tr/tr/suni-rugan-kol-cantasi-p16043010.html"
price2 = 599.95
price_URL3 = "https://www.zara.com/tr/tr/askisi-buzgulu-yarim-ay-kol-cantasi-p16050010.html"
price3 = 799.95

discount1 = Zara(price_URL1)
discount2 = Zara(price_URL2)
discount3 = Zara(price_URL3)

discount_list = [discount1, discount2, discount3]
price_list = [price1, price2, price3]


def discount_message(url, name, current_price, old_price):
    return f"İndirime Girdi YETİİİİİŞ !!!!\n************\nÜrün Adı: {name}\n Güncel Fiyat: {current_price} TL\nÖnceki Fiyat: {old_price} TL\n************\n{url}"


for disc in range(len(discount_list)):
    discount_product = discount_list[disc]
    if discount_product.price < price_list[disc]:
        discount_msg = discount_message(url=discount_product.URL,
                                        name=discount_product.name,
                                        current_price=discount_product.price,
                                        old_price=price_list[disc],
                                        )
        logger.discount(message=discount_msg)
        logger2.discount(message=discount_msg)
