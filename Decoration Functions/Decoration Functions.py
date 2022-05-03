def usalma(number):

    def inner(power):
        return number ** power

    return inner

two = usalma(2)
three = usalma(3)
print(two(3))
print(three(4))




def yetki_sorgula(page):
    def inner(role):
        if role == 'Admin':
            return "{0} rolünün {1} sayfasına ulaşabilir.".format(role, page)
        else:
            return "{0} rolünün {1} sayfasına ulaşamaz.".format(role, page)
    return inner

user1 = yetki_sorgula("Product Edit")
print(user1("Admin"))
print(user1("User"))






def islem(islem_adi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam += i
        return toplam
    def carpim(*args):
        carpim = 1
        for i in args:
            carpim *= i
        return carpim
    if islem_adi == "toplama":
        return toplam
    else:
        return carpim

toplam = islem("toplama")
print(toplam(5,5,5,5))
carpim = islem("carpim")
print(carpim(1,2,3,4,5))






def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def islem(f1, f2, f3, f4, islem_adi):
    if islem_adi == "toplama":
        print(f1(2,3))
    elif islem_adi == "cikarma":
        print(f2(5,3))
    elif islem_adi == "carpma":
        print(f3(5,5))
    elif islem_adi == "bolme":
        print(f4(10,5))
    else:
        print("Geçersiz İşlem Girildi!")

islem(toplama, cikarma, carpma, bolme, "toplama")
islem(toplama, cikarma, carpma, bolme, "cikarma")
islem(toplama, cikarma, carpma, bolme, "carpma")
islem(toplama, cikarma, carpma, bolme, "bolme")
islem(toplama, cikarma, carpma, bolme, "toplamaa")








def my_decorator(func):
    def wrapper():
        print("Fonksiyondan önceki işlemler.")
        func()
        print("Fonksiyondan sonraki işlemler")
    return wrapper

@my_decorator
def sayHello():
    print("Hello!")

sayHello()











import math
import time

def calculateTime(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)    
        func(*args,**kwargs)
        finish = time.time()
        print("Fonksiyon " + func.__name__ + " " + str(finish-start) + " Saniye Sürdü.")
    return inner
@calculateTime
def usalma(a,b):
    print(math.pow(a,b))
@calculateTime
def faktoriyel(num):
    print(math.factorial(num))
@calculateTime
def toplama(x,y):
    print(x+y)

usalma(2,10)
faktoriyel(5)
toplama(10,10)