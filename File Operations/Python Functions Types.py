#def greeting(name):
#    print("hello " + name)

#print(greeting("ali"))
#print(greeting)

#sayHello = greeting

#print(sayHello)
#print(greeting)





###### ENCAPSULATION
#def outer(num1):
#    print("outer definition online")
#    def inner_increment(num1):
#        print("inner online")
#        return num1 + 5
#    num2 = inner_increment(num1)
#    print(num1,num2)

#outer(10)







def factoriel(number):
    if not isinstance(number, int):
        raise TypeError("number must be an integer")
    elif number <= 0:
        raise ValueError("number must be zero or positive")

    def inner_factorial(number):

        if number <= 1:
            return 1

        return number * inner_factorial(number - 1)

    return print(inner_factorial(number))



try: 
    fac = input("Faktoriyelini almak istediginiz sayiyi giriniz: ")
    factoriel(fac)

except Exception as k:
    print(k)