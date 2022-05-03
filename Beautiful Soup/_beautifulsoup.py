html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>İlk Web Sayfam</title>
</head>
<body>

    <h1 id="header">
        Python Kursu
    </h1>

    <div class="grup1">
        <h2>
            Programlama
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>
    <div class="grup2">
        <h2>
            Modüller
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>    
    <div class="grup3">
        <h2>
            Fonksiyonlar
        </h2>

        <ul>
            <li>Menü 1</li>
            <li>Menü 2</li>
            <li>Menü 3</li>
        </ul>
    </div>

    <img src="Adsız.png" alt="">

    <a class="sister" href="http://example1.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example2.com/elsie" id="link1">Elsie</a>
    <a class="sister" href="http://example3.com/elsie" id="link1">Elsie</a>

</body>
</html>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc, 'html.parser')

result = soup.prettify()
##Bozulmuş html dökümanını düzeltip yazdırır.
result = soup.title
##Başlık bilgisi gelir.
result = soup.head
##Head etiketi olduğu gibi gelir.
result = soup.body
##Bütün body içeriği gelir.
result = soup.title.name
##Sadece etiket ismi gelir.
result = soup.title.string
##Etiketin içindeki ifadeyi getirir.
result = soup.h1
##h1 etiketi içerisindeki bilgilerle gelir.
result = soup.h2
##ilk h2 etiketi içerisindeki bilgilerle gelir
result = soup.h2.name
##h2 etiket ismi gelir
result = soup.h2.string
##h2 etiketinin içindeki ifade gelir.
result = soup.find_all('h2')
##bu etiket ismine ait bütün h2 etiketlerini liste şeklinde getirir.
result = soup.find_all('h2')[0]
##birinci gelir h2 etiketi gelir
result = soup.div
##div birinci etiketi gelir
result = soup.find_all('div')[1]
##ikinci div classı gelir
result = soup.find_all('div')[1].ul
##seçilen div clasın ul etiketi gelir.
result = result = soup.find_all('div')[1].ul.li
##birinci li etiketi gelir
result = result = soup.find_all('div')[1].ul.find_all('li')
##liste şeklinde li etiketlerini getirir.
result = result = soup.find_all('div')[1].ul.find_all('li')[0]
##birinci li etiketi içeriğiyle gelir.
result = soup.div.findChildren()
##div etiketindeki bütün alt elemanları getir.
result = soup.div.findNextSibling()
##ikinci div grubu gelir.
result = soup.div.findNextSibling().findNextSibling()
##üçüncü div grubu gelir.
result = soup.div.findNextSibling().findNextSibling().findPreviousSibling()
##ikinci div grubuna geri döner.
result = soup.find_all('a')
##bütün a etiketleri gelir.
result = soup.find_all('a')
for link in result:
    print(link)
##resultun a etiketlerini tek tek listeler.
for link in result:
    print(link.get('href'))
##a etiketleri içerisindeki linklere ulaşılır.
print(result)