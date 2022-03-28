## 4.DERS PYTHON OPERAT�RLER�



#a,b,c,d,e,f,g,h = 100, 200, 300, 400, 500, 600, 700, 800
#a += 5
#b -= 1
#c *= 5
#print(a, b, c, d, e, f ,g, h)
#d /= 30
#print(a, b, c, d, e, f ,g, h)
#e %= 3
#print(a, b, c, d, e, f ,g, h)
#f //= 9
#print(a, b, c, d, e, f ,g, h)
#g **= 2 
#print(a, b, c, d, e, f ,g, h)   



#values = 1, 2, 3, 4, 5
#print(values)
#print(type(values))
#x,y, *z = values
#print(x,y,z)
#print(x,y,z[2])



#x, y, z = 2, 5, 10
#a = int(input('1.Sayi Giriniz:'))
#b = int(input('2.Sayi Giriniz:'))
#result = (a*b) - (x+y+z)
#print(result)

#numbers=1,5,7,10,6
#k,*m,n = numbers
#print(m)




#a,b,c,d = 5,5,10,4
#result = a == b      #True
#print(result)
#result = a == c
#print(result)

#username = ' '
#username = input('Username: ')
#result = ( username == 'Yakupacs')
#print(result)




#a = int(input('a:  '))
#b = int(input('b:  '))
#result = (a>b)
#print(f'a: {a} b: {b} den buyuktur: {result}')



#vize1 = float(input('1.Vize notu: '))
#vize2 = float(input('2.Vize notu: '))
#final = float(input('Final notu: '))
#ortalama = (((vize1+vize2) / 2)*0.6) + (final*0.40)
#result = ortalama >= 50
#print(f'Ogrencinin ders ortalamasi: {ortalama} Derslerden gecti mi: {result} ')




#email = 'ykpacs@gmail.com'
#password = '123'

#girilenEmail = input('Mail: ')
#girilenPassword = input('Password: ')

##isEmail = (girilenEmail.strip() == email)
##isPassword = (girilenPassword == password)
#isEmailPassword = (girilenEmail.strip() == email) and (girilenPassword == password)

#print(f'Girilen Mail bilgisi Girilen Sifre bilgisi dogru mu: {isEmailPassword}' )





##MANTIKSAL OPERAT�RLER
#resultAnd = (x>5) and (x<10)  
#resultOr = (x>5) or (x<10)
#resultNot = not(x>5) 





#x = int(input('Girilen Sayi 0 ve 100 Arasinda mi? \nBir Sayi Giriniz: '))
#result = (x>0) and (x<100)
#print(result)





#x = int(input('Girilen Bir Sayinin Pozitif Cift Sayi Olup Olmadigini Bulma\nBir Sayi Giriniz: '))
#result = (x>0) and (x % 2 == 0)
#print(result)



### is operat�r� 
#x = y = [1,2,3]
#z = [1,2,3]
#print(x==y)
#print(x==z)
#print(x is y)
#print(x is z)   #ayn� adrese sahip olmas� sart.




### in operat�r�
x = ['banana','apple']
print ('banana' in x)         #x listesinde eleman sorar.