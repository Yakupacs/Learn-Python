#PYTHON DA DÖNGÜLER


#numbers = [1,2,3,4,5,6,7,8,9,10]
#for a in numbers:
#    print('Hello')



#names = ['Yakup','Ali','Muhammed','Murat']
#for name in names:
#    print(f'My name is {name}.')


#name = 'Yakup Acis'
#for a in name:
#    print(a)


#d = {'k1':1,'k2':2,'k3':3}
#for key,value in d.items():
#    print(value)



#sayilar = [1,3,5,7,9,12,19,21]

##for sayi in sayilar:
##    if(sayi%3==0):
##        print(sayi)

#toplam = 0 
#for sayi in sayilar:
#    toplam +=   sayi
#    print('toplam:',toplam)




#x = 0
#while x <= 100:
#    if (x%2 == 0):
#        print(x)
#        x += 1
#    else:
#        x += 1

#print('Program Sonlandi.')




#name = False 
#while not name.strip():
#    name = input('isminizi giriniz: ')

#print(f'Merhaba, {name} ')




#Sayilar = [1,3,5,7,9,12,19,21]

#i=0
#while (i < len(Sayilar)):
#    print(Sayilar[i])
#    i += 1





#baslangic = int(input('Baslangic: '))
#bitis = int(input('Bitis: '))
#i = baslangic
#while i< bitis:
#    i += 1
#    if (i % 2 == 1):
#        print(i)




#i = 100
#while i > 0:
#    print(i)
#    i -= 1




#number = []
#i = 0
#while i < 5:
#    sayi = int(input(f'{i+1}.Sayiyi Giriniz: '))
#    number.append(sayi)
#    i+=1
#number.sort() #elemanlari siralar. 
#print(f'5 Elemanli Listemiz: {number}')



#urunler = []
#adet = int(input('Kac urun eklemek istiyorsunuz: '))
#i = 0

#while (i<adet):
#    name = input('Urun adi: ')
#    price = float(input('Urun fiyati: '))
#    urunler.append({
#        'name' : name,
#        'price' : price
#        })
#    i += 1
#for urun in urunler:
#    print(f'Urun adi: {urun["name"]} urun fiyati: {urun["price"]}')





######BREAK

#name = 'Yakup Acis'
#for letter in  name:
#    if letter == 'k' :
#        break  
#    print(letter)



#######CONTÝNUE

#name = 'Yakup Acis'
#for letter in  name:
#    if letter == 'k' :
#        continue 
#    print(letter)




#x=1
#result = 0
#while x <= 100: 
#    x+=1
#    if x % 2 == 0:
#        continue
#    result += x
#print(f'Sayilar: {result}')


###RANGE METODU
#for item in range(50,100,10):
#    print(item)
#print(list(range(5,100,10)))



####ENUMERATE METODU
#greeting = 'Hello'
#for index,letter in enumerate(greeting):
#    print(f'index : {index} letter : {letter}')

#for item in enumerate(greeting):
#    print(item)



#####ZÝP METODU
#list1 = [1,2,3,4,5]
#list2 = ['a','b','c','d','e']
#list3 = [100,200,300,400,500]
#print(list(zip(list1,list2,list3)))

#for item in zip(list1,list2,list3):
#    print(item)

#for a,b,c in zip(list1,list2,list3):
#    print(a,b,c)







#number = []
#for x in range(10):
#    number.append(x)
#print(number)

#for x in range(10):
#    print(x**2)

#number = [x**2 for x in range(10)]
#print(number)

#number = [x*x for x in range(10) if x%3 == 0 ]
#print(number)


#myString = 'Hello'
#myList = []
#for letter in myString:
#    myList.append(letter)
#print(myList)

#myList = [letter for letter in myString]
#print(myList)







#years = [1983, 1999, 2008, 1956, 1986]
#ages = [2019-year for year in years]
#print(ages)






#results = [x if x%2==0 else 'Tek' for x in range(1,10)]
#print(results)






#result1 = []

#for x in range(3):
#    for y in range(3):
#        result1.append((x,y))
#print(result1)

#result2 = [(x,y,z) for x in range(3) for y in range(3) for z in range(3)]
#print(result2)







######                                                                                                    SAYI TAHMÝN OYUNU
#import random
#randomSayi = random.randint(1,100)
#can = int(input('Kac Hakkiniz Olsun: '))
#hak = can
#sayac = 0
#while hak>0:
#    hak -= 1
#    sayac += 1
#    tahmin = int(input('Bir tahmin giriniz: '))
#    if randomSayi == tahmin:
#        print(f'Tebrikler {sayac}. Hakkinizda Dogru Bildiniz. Toplam Puaniniz: {100 - (100/can) * (sayac-1)}')
#        break
#    elif randomSayi > tahmin:
#        print('Yukari Cik.')
#    else:
#        print('Asagi In.')
#    if hak == 0:
#        print(f'Hakkiniz Bitti. Tutulan Sayi {randomSayi}')










#Sayi = int(input('Bir Sayi Giriniz: '))
#asalmi = True
#if Sayi == 1:
#    print(f'{Sayi} Sayisi Asal Degildir.')
#elif Sayi<0:
#    print(f'{Sayi} Sayisi Negatiftir.')
#    asalmi = False
#elif Sayi == 0:
#    print(f'{Sayi} Sayisi Sifirdir.')
#    asalmi = False

#for i in range(2, Sayi):
#    if (Sayi % i == 0):
#        asalmi = False
#        break

#if asalmi:
#    print(f'{Sayi} Sayisi asaldir.')
#else:
#    print(f'{Sayi} Sayisi asal degildir.')