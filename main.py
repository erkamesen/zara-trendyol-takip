from telegram import Logger
from shop import Shop
from dotenv import load_dotenv
import os

load_dotenv()


# TELEGRAM API KEY VE CHATID GİR
# 2 ADET HESABA ATTIĞIM İÇİN 2 ADET LOGGER KULLANDIM
logger = Logger(
    token=os.getenv("APIKey"), chat_id=os.getenv('chatID1'))
logger2 = Logger(
    token=os.getenv("APIKey"), chat_id=os.getenv("chatID2"))


## MESSAGE UTILS ##
def stock_message(url, name, price):
    return f"Stoğa Girdi !!!!\n⬇⬇⬇⬇⬇\nÜrün Adı: {name}\nGüncel Fiyat: {price} TL\n⬆⬆⬆⬆⬆\n{url}"


def discount_message(url, name, current_price, old_price):
    return f"İndirime Girdi YETİİİİİŞ !!!!\n⬇⬇⬇⬇⬇\nÜrün Adı: {name}\nGüncel Fiyat: {current_price} TL\nÖnceki Fiyat: {old_price} TL\n⬆⬆⬆⬆⬆\n{url}"


""" STOK TAKİBİ """

stock_URL1 = "https://www.zara.com/tr/tr/share/-p04387241.html?utm_campaign=productMultiShare&utm_medium=mobile_sharing_iOS&utm_source=red_social_movil&v1=223811112"

stock1 = Shop(stock_URL1)


for product in Shop.stock_list:
    try:
        if product.is_stock:
            stock_msg = stock_message(
                url=product.URL,
                name=product.name,
                price=product.price
            )
            logger.info(message=stock_msg)
            logger2.info(message=stock_msg)
    except:
        logger.warning(
            message=f"{product.name} URL ile ilgili sıkıntı var yetiş {product.URL}")
        continue


""" FİYAT TAKİBİ """

# Fiyat takibi için URL lerimizi ve fiyatlarımızı giriyoruz.
price_URL1 = "https://www.zara.com/tr/tr/zw-90-s-wide-leg-suni-deri-pantolon-p02969242.html"
price1 = 659.95


# URL lerimizden nesnelerimizi oluşturuyoruz.
discount1 = Shop(price_URL1, price_check=True)

# Fiyatlarımızı listemizde topluyoruz.
price_list = [price1]


for sira, disc in enumerate(Shop.discount_list):
    discount_product = Shop.discount_list[sira]
    try:
        if float(discount_product.price) < price_list[sira]:
            print(discount_product.price, price_list[sira])
            discount_msg = discount_message(
                url=discount_product.URL,
                name=discount_product.name,
                current_price=discount_product.price,
                old_price=price_list[sira],
            )
            logger.discount(message=discount_msg)
            logger2.discount(message=discount_msg)
    except:
        logger.warning(
            message=f"{discount_product.name} Ürünle ile ilgili sıkıntı var yetiş {discount_product.URL}")
        continue
