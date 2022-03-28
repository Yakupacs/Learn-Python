#Object Oriented Programming (OOP)


 ##class => Person (name, surname, birthday, calculatorAge)
 ##instance(object)

#lst1= [1,2,3]
#lst2 = [1,2,3,4]

#print(type(lst1))
#print(type(lst2))





###class
#class Person:
#    #class attritubes
#    address = 'No Information'
#    #constrcutor (yapýcý metod)
#    def __init__(self,name,year):
#        #object attributes
#        self.name = name
#        self.year = year
#        print('Init Metodu Calisti.')
#    # instance methods
#    def intro(self):
#        print('Hello There. I am ' + self.name )
#    # instance methods
#    def calculateAge(self):
#        return 2021 - self.year  

##objects (instance)
#p1 = Person(name = 'Yakup',year = 2000)
#p2 = Person(name = 'Abdulkadir',year = 1969)
## updating
#p2.name='Muhammed'
#p2.year=2001
## accessing object attritubes
#print(f"p1\nName: {p1.name} \nYear: {p1.year}\nAdres: {p1.address}")
#print(f"p2\nName: {p2.name} \nYear: {p2.year}\nAdres: {p1.address}")

#print(p1,p2)
#print(type(p1),type(p2))
#print(p1 == p2)
#p1.intro()
#p2.intro()
#p1.calculateAge()
#print(f"Adim {p1.name} ve yasim {p1.calculateAge()}")
#print(f"Adim {p2.name} ve Yasim {p2.calculateAge()}")





#class Circle:
#    #Class object attribute
#    pi = 3.14

#    def __init__(self, yaricap=1):
#        self.yaricap = yaricap

#    #Methods
#    def cevre_hesapla(self):
#        return 2*self.pi * self.yaricap  

#    def alan_hesapla(self):
#        return self.pi * (self.yaricap**2) 

#c1 = Circle()   #yaricap 1
#c2 = Circle(5)

#print(f'c1 alan: {c1.alan_hesapla()} ,c1 cevre: {c1.cevre_hesapla()}')
#print(f'c2 alan: {c2.alan_hesapla()} ,c2 cevre: {c2.cevre_hesapla()}')




# Inheritance (Kalýtým) : Miras Alma

# Person => name, lastname, age, eat(), run(), drink()
# Student(person), Teacher(person)

# Animal => Dog(Animal), Cat(Animal)







#class Person:
#    def __init__(self,fname,lname):
#        self.firstName = fname
#        self.lastName = lname   
#        print('Person Created.')
#    def who_am_i(self):
#        print('I am person.')

#class Student(Person):
    
#    def __init__(self, fname, lname, number):
#        Person.__init__(self,fname,lname)
#        self.studentNumber = number
#        print('Student Created.')
#    #override
#    def who_am_i(self):
#        print('I am student.')
#    def sayHello(self):
#        print('Hello There. I am a student. ')

#class Teacher(Person):

#    def __init__(self, fname, lname,branch):
#        super().__init__(fname,lname)
#        self.branch = branch

#    def who_am_i(self):
#        print(f'Hello, I am a {self.branch} teacher.')

#p1 = Person('Ali','Yilmaz')
#s1 = Student('Yakup','Mehmet',12345)
#t1 = Teacher('Nevin','Yildirim','Math')

#print(p1.firstName + ' ' + p1.lastName)
#print(s1.firstName + ' ' + s1.lastName + ' ' + str(s1.studentNumber))

#p1.who_am_i()
#s1.who_am_i()
#s1.sayHello()
#t1.who_am_i()








#myList = [1,2,3]

#class Movie():
#    def __init__(self, title, director, duration):
#        self.title = title
#        self.director = director
#        self.duration = duration
#        print('Movie is created.')

#    def __str__(self):
#        return f'{self.title} by {self.director}.'

#    def __len__(self):
#        return self.duration

#    def __del__(self):
#        print('Movie is deleted.')

#m = Movie('Esaretin Bedeli', 'Frank Darabont', 120)
##print(len(m))
##print(myList)
#print(m)
#del m