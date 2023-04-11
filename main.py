from telegram import Logger
from shop import Shop
from dotenv import load_dotenv
import os

load_dotenv()


# TELEGRAM API KEY VE CHATID GİR
logger = Logger(
    token=os.getenv("APIKey"), chat_id=os.getenv('chatID1'))



## MESSAGE UTILS ##
def stock_message(url, name, price):
    return f"Stoğa Girdi !!!!\n⬇⬇⬇⬇⬇\nÜrün Adı: {name}\nGüncel Fiyat: {price} TL\n⬆⬆⬆⬆⬆\n{url}"


def discount_message(url, name, current_price, old_price):
    return f"İndirime Girdi YETİİİİİŞ !!!!\n⬇⬇⬇⬇⬇\nÜrün Adı: {name}\nGüncel Fiyat: {current_price} TL\nÖnceki Fiyat: {old_price} TL\n⬆⬆⬆⬆⬆\n{url}"


""" STOK TAKİBİ """

""" STOK TAKİBİ YAPACAĞNIZ ÜRÜNLERİ AŞAĞIDAKİ GİBİ EKLEYİN """

stock_URL1 = "https://www.zara.com/tr/tr/desenli-keten-karisimli-midi-elbise-p03286781.html?v1=255317336&v2=2184287"
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
    
    except:
        logger.warning(
            message=f"{product.name} URL ile ilgili sıkıntı var yetiş {product.URL}")
        continue


""" FİYAT TAKİBİ """

# Fiyat takibi için URL lerimizi ve fiyatlarımızı giriyoruz.
price_URL1 = "https://www.trendyol.com/trendyolmilla/siyah-straight-dokuma-yuksek-bel-nervur-dikisli-pantolon-twoss21pl0093-p-71519125?boutiqueId=620236&merchantId=968&sav=true"
price1 = 167.99


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
    except:
        logger.warning(
            message=f"{discount_product.name} Ürünle ile ilgili sıkıntı var yetiş {discount_product.URL}")
        continue
