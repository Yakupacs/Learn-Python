#İLK 1,2,3 DERS



#print("merhaba")
#print(2+2)
#print(2+2.2)
#print(type(2))
#print(type(2.4))
#print(2+2*10+2)
#print(2**4)
#print(10%3)
#print(10//3)
#maasAli = 5000
#maasAhmet = 4000
#vergi = 0.27
#print(maasAli - (maasAli * vergi))
#print(maasAhmet - (maasAhmet * vergi))
#number1 = 10
#print(number1)
#number1 = 20
#print(number1)
#number1 += 30
#print(number1)
#x=1                #int
#y=2.3              #float
#name = "Çınar"     #string
#isStudent = True   #bool
##x, y, name, isStudent = (1, 2.3, "Çınar", True)




#MÜŞTERİ BİLGİSİ OLUŞTURMA
#musteriAd = 'Yakup'
#musteriSoyad = 'Acis'
#musteriAdSoyad = musteriAd + ' ' + musteriSoyad
#musteriCinsiyet = True #Erkek
#musteriTC = '12345678912'
#musteriDogumYili = 2000
#musteriAdres = 'istanbul'
#musteriYasi = 2021 - musteriDogumYili
#print(musteriAdSoyad, musteriTC, musteriAdres)




#İKİ SAYIYI TOPLAMA 
#x = input('1.Sayiyi Giriniz: ')
#y = input('2.Sayiyi Giriniz: ')
#print(type(x))
#print(type(y))
#toplam = int(x) + int(y)
#print(toplam)




#int to float 
#x = 12
#x = float(x)
#print(x)
#print(type(x))




#float to int
#y = 2.5
#y = int(y)
#print(y)
#print(type(y))



#bool to str
#isOnline = True
#print(isOnline)
#print(type(isOnline))
#isOnline = str(isOnline)
#print(isOnline)
#print(type(isOnline))




#bool to int
#isOnline = False
#isOnline = int(isOnline)
#print(isOnline)
#print(type(isOnline))





#pi = 3.14
#r = float(input("Yaricapi Giriniz : "))
#alan = pi * (r ** 2)
#cevre = 2 * pi * r
#print("Dairenin alani :",alan)
#print("Dairenin cevresi :",cevre)
#print("Alan : " + str(alan) + " Cevre : " + str(cevre))







#name = 'Yakup' 
#surname = 'Acis'
#age = 21 
#print ('My name is ' + name + ' ' + surname + ' and \nI am ' + str(age) + ' years old')
#greeting = 'My name is ' + name + ' ' + surname + ' and \nI am ' + str(age) + ' years old'
#length = len(greeting) 
#print(greeting[0])                 #sıfırdan başlar
#print(greeting[5])
#print(len(greeting))
#print(greeting[length-1])      #son karakteri bulur.
#print(greeting[-1])                #son karakteri bulur.
#print(greeting[3:7])             #üçüncü indeksten yedinci indeksi yazar.
#print(greeting[3: ])              #üçten başlar sona kadar gider.
#print(greeting[ :13 ])           #baştan 13 e kadar gider.
#print(greeting[0:40:2 ])      #iki karakterde bir yazar.






#name = 'Yakup'
#surName = 'Acis'
#age = '21'
#print("My name is {} {} and I'm {} years old.".format(name, surName, age))    #formatta tür dönüşümü yapmaya gerek kalmaz.
#result= 200/ 700
#print('The result is {r:1.4}'.format(r=result))
#print(f"My name is {name} {surName} and I'm {age} years old.")






## 'course' karakter dizisinde kaç karakter bulunmaktadır?
#website = "http://www.sadikturan.com"
#course = "Pyhton Kursu: Bastan Sona Python Programlama Rehberiniz (40 saat)"
#length = len(website)
#result = len(course)
#print(result)
#result = website[7:10]
#print(result)
#result = website[22:25]
#print(result)
#result = website[length-3:length]
#print(result)
#result = course[::-1]             #tersten yazar
#print(result)





message = " Hello There. My name is Yakup Acis"

##message = message.upper()           #bütün kelimeler büyük harf
##print(message)
##message = message.lower()           #bütün kelimeler küçük harf
##print(message)
##message = message.title()           #her kelimenin baş harfi büyür.
##print(message)
##message = message.capitalize()   #sadece ilk harf büyük olur
##print(message)
##message = message.strip()              #baştaki ve sondaki boşluğu siler.
##print(message)                          
##message = message.split()           #kelimeleri ayırır.
##print(message)
##message = ' '.join(message)            #kelimeleri birleştirir
##print(message)
##index = message.find('yakup')           #belirtilen kelimenin kaçıncı satırdan itibaren başladığını söyler.
##print(index)
##isFound = message.startswith('h')      #bu harfle başlarsa true
##print(isFound)
##isFound = message.endswith('s')         #bu harfle biterse true
##print(isFound)
##message = message.replace('a','e').replace('i','e')       #kelimeyi veya harfi değiştirir
##print(message)
##message = message.center(100,'*')           #100 boş karakter oluşturur sağa ve sola
##print(message)





#userA = ['Yakup',21]
#userB = ['Muhammed',20]
#users = [userA,userB]
#print(users[0][0])






arabalar = ['Bmw','Mercedes','Opel','Mazda']
result = len(arabalar)
print(result)
arabalar[0] = 'Bmw 4.7'
result1 = arabalar
print(result1)
result2 = 'Mercedes' in arabalar        #arabalar listesinde Mercedes var mı?
print(result2)
arabalar[-2:] = ['Toyota','Renault']    #son iki elemanı değiştir.
result3 = arabalar
print(result3)
result4 = arabalar + ['Audi','Nissan']
print(result4)
del arabalar[-1]                                    #son elemanı sil
result5 = arabalar
print(result5)
result6 = arabalar[::-1]                        #tersten yazar
print(result6)






#studentA = ['Yigit','Bilgi',2010,[70,60,70]]
#studentB = ['Sena','Turan',1999,[80,80,70]]
#studentC= ['Ahmet','Turan',1998,[80,70,90]]
#result = f"{studentA[0]} {studentA[1]} {2021-studentA[2]} yasinda ve not ortalamasi {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3} "
#print(result)





#numbers =    [1,10,5,16,4,9,10]
#letters = ['a','g','s','b','y','a','s']
#val1 = min(numbers)
#val2 = max(numbers)
#val3 = min(letters)
#val4 = max(letters)
#print(val1, val2, val3, val4)
#numbers.append(49)                  #listenin en sonuna ekler
#numbers.append(59)
#numbers.insert(3,99)                #3 den sonra 99 ekler.
#numbers.pop()                           #en sondaki elemanı siler
#numbers.pop(0)                          #baştaki elemanı siler
#numbers.remove(5)                      #5 rakamını siler.
#numbers.sort()                          #sayısal olarak sıralanır.
#numbers.reverse()                   #listeyi olduğu gibi ters çevirir.
##numbers.clear()                         #elemanları temizler.
#print(numbers.count(10))        #kaç tane 10 olduğunu gösterir.
#print(numbers)






#names = ['Ali','Yagmur','Hakan','Deniz']
#years = [1998, 2000, 1998, 1987]
#names.append('Cenk')
#print(names)
#names.insert(0, 'Sena')
#print(names)
#names.insert(len(names), 'Mehmet')
#print(names)
#names.remove('Deniz')
#print(names)
#listeElemanimi = 'Ali' in names
#print(listeElemanimi)
#yearsMin = min(years)
#yearsMax = max(years)
#print(yearsMin,yearsMax)





#markalar = []
#marka=input("1.Marka Giriniz : ")
#markalar.append(marka)
#marka=input("2.Marka Giriniz : ")
#markalar.append(marka)
#marka=input("3.Marka Giriniz : ")
#markalar.append(marka)
#print(markalar)





##TUPLE LİSTE
#list = ['Ayse','Beril','Cemre']
#list2 = ['Deniz','Elif','Helin'] + list
#tuple = ('Ayse','Beril', 'Cemre')
#tuple2 = ('Deniz','Elif','Helin') + tuple
#print(type(list))
#print(type(tuple)) 
#print(list[1])
#print(tuple[1])
#print(len(list))
#print(len(tuple))
#list[0] = 'Mehmet'
##tuple[0] = Mehmet    #tuplede elemanı atayarak değiştiremezsiniz.
#print(list)
#print(list2)
#print(tuple)
#print(tuple2)
##Tek farkı liste üzerinde eleman değiştirme işlemi yapılamaz





#plakalar = { 'Kocaeli' : 41 , 'Istanbul' : 34 }
#print(plakalar['Kocaeli'])
#print(plakalar['Istanbul'])
#plakalar['Ankara'] = 6
#print(plakalar)






#users = {
#    'Yakup' : {
#        'age' : 21,
#        'telephone' : '2132132132'},
#    'Muhammed' : {
#        'age' : 20,
#        'telephone' : '214214214'}
#      }
#print(users['Yakup'])





ogrenciler = {}
number = input('Ogrenci No: ')
name = input('Ogrenci Adi: ')
surname = input('Ogrenci Soyadi: ')
phone = input('Ogrenci Telefonu: ')

#ogrenciler[number] = {
#    'Ad' : name,
#    'Soyad' : surname,
#    'Telefon' : phone}

ogrenciler.update({
    number: {
        'Ad' : name,
        'Soyad' : surname,
        'Telefon' : phone}})

#number = input('Ogrenci No: ')
#name = input('Ogrenci Adi: ')
#surname = input('Ogrenci Soyadi: ')
#phone = input('Ogrenci Telefonu: ')
 
#ogrenciler.update({
#    number: {
#        'Ad' : name,
#        'Soyad' : surname,
#        'Telefon' : phone}}) 

#number = input('Ogrenci No: ')
#name = input('Ogrenci Adi: ')
#surname = input('Ogrenci Soyadi: ')
#phone = input('Ogrenci Telefonu: ')
 
#ogrenciler.update({
#    number: {
#        'Ad' : name,
#        'Soyad' : surname,
#        'Telefon' : phone}}) 

print(ogrenciler)

ogrNo = input('Ogrenci No: ')
#ogrenci = ogrenciler[ogrNo]
print(ogrenciler[ogrNo])






#fruits  = {'apple','banana','orange'}
#print(fruits)
#fruits.add('cherry')
#fruits.update(['mango','grape','apple'])   
#print(fruits)
#fruits.remove('mango')
#fruits.discard('apple')
#print(fruits)





###value types => string, number
#x = 5
#y = 25
#print(x,y)
#x = y 
#print(x,y)
#y = 10
#print(x,y)
###reference types => list
#a = ['apple','banana']
#b = ['apple','banana']
#a = b
#b[0] = 'grape'
#print(a,b)








