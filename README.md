# Zara-Trendyol Takip Botu
Zara - Trendyol  Telegram Bildirimli Stok Fiyat Takip Botu


## Kullanım:
Terminal üzerinden:
- git clone https://github.com/erkamesen/Zara-TakipBotu.git (Bulunduğunuz dizine kopyasını oluşturma) 
- cd zara-trendyol-takip (Oluşturulan dizinin içine giriyoruz.)
- Linux - MacOS
```
python3 main.py
```
- Windows
```
python main.py
```

Zara classından oluşturduğunuz nesnelerinize parametre olarak ürünlerin URL lerini vererek belirtilen ürünleri takibe alabilirsiniz. 
Telegram dan aldığınız APIKey i ve chatID nizi Logger sınıfından ürettiğimiz logger nesnelerine paramertre olarak vererek telegram bildirimi sağlayabilirsiniz.
```
logger = Logger(
    token=APIKey, chat_id=ChatID)

```
Telegram Bot oluşturmak için [BotFather](https://t.me/BotFather)'a aşağıdaki komutları yazmanız yeterli:
- /start
- /newbot
- Bota bir isim verin
- Bota unique bir kullanıcı adı belirleyin

Botumuzu oluşturduk şimdi gelen mesajda <br>
"Use this token to access the HTTP API:" kısmının hemen altında yazan key bizim APIKeyimiz. <br>

APIKey imizi de aldığımıza göre farklı işlevler için de burayı kullanabilirsiniz.
[Telegram API](https://core.telegram.org/api)


**Ürün stoğa girince gelen mesaj** <br>
![Seçim_036](https://user-images.githubusercontent.com/120065120/214649654-28dd593b-2dfd-432c-b069-4edb5261d503.png)

***

**Ürün indirime girince gelen mesaj** <br>
![Seçim_037](https://user-images.githubusercontent.com/120065120/214649799-182d2792-7578-47ea-ac0f-b599a60667d2.png)

***

## Crontab - Linux

Yazdığımız bu scripti elle çalıştırarak kontrol etmek oldukça zahmetli ve bir o kadar anlamsız olacağından ya remote olarak [pythonanywhere](https://www.pythonanywhere.com) gibi
platformları ya da bilgisayarımızda crontab gibi kendi istemcimiz üzerinde çalışan servisleri kullanabiliriz.
Kısaca: <br>
Crontab linux sistemlerinde kullanılan bir servistir. Crontab bir komutu, scripti ya da uygulamayı belirlediğiniz zaman
veya belirli zaman aralıklarıyla çalışmasını sağlamaktadır. <br>


- Terminalimizi açıyoruz.
```
which python3
# /usr/bin/python3
```
- Python konumumuzu öğrendik. crontab ı aktif edelim.
```
crontab -e
```
- Açılan kısımdan en baştaki -easiest olanı seçiyoruz.Böyle bir sayfa görmeniz lazım.
![Seçim_038](https://user-images.githubusercontent.com/120065120/214651904-e2a786cc-f468-46db-802a-333a0aee86ea.png)

- En alt kısıma iniyoruz.
```
*/3 * * * * /usr/bin/python3 /home/erkam/Flask/Zara/main.py
```
- */3 * * * * = Her 3 dakikada bir çalışıcak. Zaman ayarı için [tıklayınız](https://crontab.guru/).
- /usr/bin/python3 = Python PATH
- /home/erkam/Flask/Zara/main.py = Python dosyamızın PATH i
- Çalışan scriptleri görmek için:
```
crontab -l

```
![Seçim_039](https://user-images.githubusercontent.com/120065120/214652636-c16e3413-88f8-469d-aa10-deac7cb567ff.png)


## Task Scheduler - Windows

Kendisini hiç kullanmadım. Sadece alternatifini aramayın diye yazıyorum. 
[Buradan](https://www.hakanuzuner.com/powershell-scriptleri-icin-gorev-zamanlayiciyi-task-scheduler/) yardım alabilirsiniz.






