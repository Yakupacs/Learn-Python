#error => hata

#error handling => hata yönetimi

#Error
#print(a) => NameError
#int('1a2') => ValueError
#print(10/0) => ZeroDivisionError
#print('denem'e) => SyntaxError







#while True:
#        try:
#            x = int(input('x: '))
#            y = int(input('y: '))
#            print(x/y)

#        #except ZeroDivisionError:
#        #    print('Y sifir olamaz!')

#        except Exception as exp:
#            print(f'Hata: {exp}')

#        else:
#            break

#        finally:
#            print('Hata Kontrolu Basarili!')









#x = 10

#if x > 5:
#    raise Exception('x 5 ten buyuk deger alamaz.')


#def check_password(psw):
#    import re
#    if len(psw) < 7:
#        raise Exception("parola en az 7 karakter olmalidir.")
#    elif not re.search("[a-z]", psw):
#        raise Exception("parola kucuk harf icermelidir.")   
#    elif not re.search("[A-Z]", psw):
#        raise Exception("parola buyuk harf icermelidir.")
#    elif not re.search("[0-9]", psw):
#        raise Exception("parola rakam harf icermelidir.")    
#    elif not re.search("[_@$]", psw):
#        raise Exception("parola alpha numeric icermelidir.")    
#    elif not re.search("[_@$]", psw):
#        raise Exception("parola alpha numeric icermelidir.")    
#    elif re.search("\s", psw):
#        raise Exception("parola bosluk icermemelidir.")
#    else:
#        print("Parola Basarili!")

#password = input("parola: ")

#try:
#    check_password(password)
#except Exception as ex:
#    print(ex)











#class Person:
#    def __init__(self, name, year ):
#        if len(name) > 10:

#            raise Exception("name alani fazla karakter iceriyor.")

#        else:

#            self.name = name
#            self.year = year


#Person("ALiiiiffgfgiii", 1989) 

 




#liste = ["1","2","5a","10b","abc","10","50"]

#for x in liste:
#    try:
#        result = int(x)
#        print(f'Basarili Sayi: {result}')
#    except Exception as a:
#        print(a)
#        continue



#while True:
#    sayi = input('Sayi Giriniz: ')
#    if sayi == 'q':
#        break
   
#    try:
#        result = float(sayi)
#        print('Girdiginiz sayi: ', result)
#    except ValueError:
#        print('Gecersiz Sayi!')
#        continue







#def checkPassword(parola):
#        turkce_karakterler='þçðüýÝ'

#        for i in parola:
#            if i in turkce_karakterler:
#                raise TypeError('Parola Turkce Karakter iceremez.')
#            else:
#                pass
#        print('basarili parola')

#parola = input('Parola: ')

#try:
#    checkPassword(parola)
#except TypeError as err:
#    print(err)





#def faktoriyel(x):
#    x = int(x)

#    if 0 > x:
#        raise ValueError('Girdiginiz sayi 0"dan kucuk olamaz.')

#    result = 1

#    for i in range(1, x+1):
#        result *= i

#    return result

#for x in [5, 10, 20, -3, '10a']:

#    try:
#        y = faktoriyel(x)
#        print('basarili',x)
#    except ValueError as err:
#        print(err)
#        continue
#    print(y)