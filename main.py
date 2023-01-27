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
stock_URL2 = "https://www.zara.com/tr/tr/share/-p01255896.html?utm_campaign=productMultiShare&utm_medium=mobile_sharing_iOS&utm_source=red_social_movil&v1=224850511"
stock_URL3 = "https://www.zara.com/tr/tr/share/-p01255825.html?utm_campaign=productMultiShare&utm_medium=mobile_sharing_iOS&utm_source=red_social_movil&v1=186613774"
stock_URL4 = "https://www.zara.com/tr/tr/share/-p05854714.html?utm_campaign=productMultiShare&utm_medium=mobile_sharing_iOS&utm_source=red_social_movil&v1=178078856"
stock_URL5 = "https://www.zara.com/tr/tr/share/-p03046274.html?utm_campaign=productMultiShare&utm_medium=mobile_sharing_iOS&utm_source=red_social_movil&v1=223692936"
stock_URL6 = "https://www.zara.com/tr/tr/share/-p03046313.html?utm_campaign=productMultiShare &utm_medium=mobile_sharing_iOS&utm_source=red_social_movil&v1=188530143"
stock_URL7 = "https://www.zara.com/tr/tr/suni-deri-oversize-ceket-p03427811.html?utm_campaign=productMultiShare&utm_medium=mobile_sharing_iOS&utm_source=red_social_movil&v1=186019786"
stock_URL8 = "https://www.trendyol.com/stradivarius/suni-kurk-ceket-p-453223690?boutiqueId=618534&merchantId=150331&utm_source=share"


stock1 = Shop(stock_URL1)
stock2 = Shop(stock_URL2)
stock3 = Shop(stock_URL3)
stock4 = Shop(stock_URL4)
stock5 = Shop(stock_URL5)
stock6 = Shop(stock_URL6)
stock7 = Shop(stock_URL7)
stock8 = Shop(stock_URL8)


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
price_URL2 = "https://www.zara.com/tr/tr/suni-rugan-kol-cantasi-p16043010.html"
price2 = 599.95
price_URL3 = "https://www.zara.com/tr/tr/askisi-buzgulu-yarim-ay-kol-cantasi-p16050010.html"
price3 = 799.95
price_URL4 = "https://www.trendyol.com/stradivarius/5-cepli-suni-deri-timsah-desenli-pantolon-p-372037428?boutiqueId=618534&merchantId=150331&utm_source=share"
price4 = 299.95


# URL lerimizden nesnelerimizi oluşturuyoruz.
discount1 = Shop(price_URL1, price_check=True)
discount2 = Shop(price_URL2, price_check=True)
discount3 = Shop(price_URL3, price_check=True)
discount4 = Shop(price_URL4, price_check=True)
# Fiyatlarımızı listemizde topluyoruz.
price_list = [price1, price2, price3, price4]


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
