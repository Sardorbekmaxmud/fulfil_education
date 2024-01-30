# class Student:
#     def __init__(self, name):
#         print("Konstruktir ichi __init__()")
#         self.name = name
#         print("Hamma o'zgaruchilar ishga tushurildi")
#
#     def show(self):
#         print("Hello, my name is", self.name)
#
#
# # Konstruktirni ishlatib obyekt yaratish
# stu1 = Student("Emma")
# stu1.show()


# default constructor
# class Employee:
#     def display(self):
#         print("Inside Display or", r"Ichki Display")
#
# emp = Employee()
# emp.display()


# Non-parametrized - Parametrsiz
# class Company:
#     def __init__(self):
#         self.name = "Artel"
#         self.address = "Tashkent, Shayxantaxur"
#
#     def show(self):
#         print(f"Name: {self.name}, Address: {self.address}")
#
#
# comp = Company()
# comp.name = "Hyatt-hotel"
# comp.address = "Tashkent, Mirzo Ulug'bek"
# comp.show()


# Parametrized Constructor - Parametrli konstruktor
# class Employee:
#     def __init__(self, name, age, salary):
#         print("Call konstruktor")
#         self.name = name
#         self.age = age
#         self.salary = salary
#
#     def show(self):
#         print(self.name, self.age, self.salary)
#
#
# emma = Employee("Emma", 23, 7500)
# emma.show()
#
# georgi = Employee("Georgi", 25, 8500)
# georgi.show()


## KOnsruktorga defult qiymat berish
# class Student:
#     def __init__(self, name, age=19, classroom=32):
#         self.name = name
#         self.age = age
#         self.classroom = classroom
#
#     def show(self):
#         print(self.name, self.age, self.classroom)
#
#
# s1 = Student("Emma")
# s1.show()
#
# s2 = Student("Doe", 20)
# s2.show()
#
# s3 = Student("Obama", 24, 12)
# s3.show()


# class Vehicle:
#     def __init__(self, engine):
#         print("Ichi Vehicle Konstruktori")
#         self.engine = engine
#
#
# class Car(Vehicle):
#     def __init__(self, engine, max_speed):
#         super().__init__(engine)
#         print("Ichki Car Konstruktori")
#         self.max_speed = max_speed
#
#
# class ElectricCar(Car):
#     def __init__(self, engine, max_speed, km_range):
#         super().__init__(engine, max_speed)
#         print("Ichki ElectricCar Konstruktori")
#         self.km_range = km_range
#
#
# ev = ElectricCar(5.5, 350, 650)
# print(f"Engine={ev.engine}, Max speed={ev.max_speed}, Km range={ev.km_range}")


# class Employee:
#     count = 0
#
#     def __init__(self):
#         Employee.count += 1
#
#
# e1 = Employee
# e2 = Employee
# e3 = Employee
#
# print(Employee.count)


##Destructor - del
# class Student:
#     #konstruktir - constructor
#     def __init__(self, name):
#         print("Konstruktir ichida")
#         self.name = name
#         print("Obyekt ishga tushdi")
#
#     def show(self):
#         print(f"Hello, my name is {self.name}")
#
#     # destructor -- buzuvchi -- o'chiruvchi
#     def __del__(self):
#         print("Destruktir ichida")
#         print("Obyekt o'chirildi")


# s1 = Student("Emma")
# s1.show()


##-==-=-=-=-=-=-=-=-=Vorisdorlik - Inhertance, Polimorfizm-=-=-=-=-=--=-=-=-=-=-=-=-
# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def speak(self, words):
#         print(f"{self.name} speaks: {words}")
#
#
# class Employee(Person):
#     def __init__(self, name, age, gender, salary, job_title):
#         super().__init__(name, age, gender)
#         self.salary = salary
#         self.job_title = job_title
#
#     def display_info(self):
#         print(f"Employee {self.name} works as a {self.job_title}")


# em1 = Employee("Georgio", 26, "male", "Computer Science", "Programmer")
# em1.speak("I am a programmer")
# em1.display_info()


# class Base:
#     def call(self):
#         print("Base Class")
#
#
# class Left(Base):
#     def call(self):
#         print("Left Class")


# class Right(Base):
#     def call(self):
#         print("Right Class")
#
#
# class Child(Left, Right):
#     pass


# ch1 = Child()
# ch1.call() #method resolution order
# print(Child.mro())


# class Vehicle:
#     def __init__(self, name, color, price):
#         self.name = name
#         self.color = color
#         self.price = price
#
#     def show(self):
#         print(f"Details: {self.name} {self.color} {self.price}")
#
#     def max_speed(self):
#         print("Vehicle max speed is 150")
#
#     def change_gear(self):
#         print("Vehicle change 6 gear")
#
#
# class Car(Vehicle):
#     def max_speed(self):
#         print("Car max speed is 240")
#
#     def change_gear(self):
#         print("Car change 7 gear")


# car1 = Car("BMW X6", "Cyan", 200_000)
# car1.show()
# car1.max_speed()
# car1.change_gear()
# print()
#
# vehicle1 = Vehicle("Volvo FH1", "Gray", 450_0000)
# vehicle1.show()
# vehicle1.max_speed()
# vehicle1.change_gear()


# class Shopping:
#     # __slots__ = ['basket', "buyer"]
#     def __init__(self, basket, buyer):
#         self.basket = basket
#         self.buyer = buyer
#
#     def __len__(self):
#         print("Uzunlikni qayta belgilang")
#         count = len(self.basket)
#         return count * 2
#
#     def __str__(self):
#         return f"{self.buyer}"


# shopping = Shopping(['shoes', 'dress'], "Jessa")
# print(len(shopping))
# print(shopping)


##-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=F-18 OOP-2 -=-=-=-=--=-=-=-=-=-=-===-==-=-=-=-=-=
# class Avto:
#     def __init__(self, model, color, year):
#         self.model = model
#         self.color = color
#         self.year = year
#
#     def __repr__(self):
#         return f"{self.color} {self.model} {self.year} yil"
#
#
# avto_1 = Avto("Nexia", "Oq", 1996)
# avto_2 = Avto("Equinox", "Ko'k", 2023)
#
# print(avto_1)
# print(avto_2)


# class Person:
#     def __init__(self, name: str, age: int, is_boy: bool):
#         self.name = name
#         self.age = age
#         self.is_boy = is_boy
#
#     def __add__(self, other):
#         return f"{self.name} + {other.name} = S"
#
#     def __sub__(self, other):
#         return f"{self.name} endi yolg'iz bo'ri. {other.name} xolasinikiga ketdi."
#
#     def __pow__(self, power, modulo=None):
#         return f"{power.name}xon ** {self.name}jonlarning nikoh to'ylariga xush kelibsiz!"
#
#     def __mul__(self, other):
#         return f"{self.name} * {other.name} bolali bo'lishdi."
#
#     def __truediv__(self, other):
#         return f"{self.name} / {other.name} urushib qolishdi."
#
#     def __repr__(self):
#         return f"{self.name}"
#
#     def __len__(self):
#         print(f"{self.name} ismi uzunligi: ", end="")
#         return len(self.name)
#
#     def __int__(self):
#         print(f"{self.name}ning yoshi ", end="")
#         return self.age
#
#
#
# paloncha = Person("Akmal", 24, True)
# tuguncha = Person("Gulshoda", 21, False)
# print(paloncha + tuguncha)
# print(paloncha - tuguncha)
# print(paloncha ** tuguncha)
# print(paloncha * tuguncha)
# print(paloncha / tuguncha)
# print(len(paloncha))
# print(str(paloncha))
# print(repr(paloncha))
# print(int(paloncha))
#
# print(paloncha.__dict__["is_boy"])


##-================---------sariq.dev dunder metodlar qo'shimcha------==========-----===-----------=========
class Avto:
    __num_avto = 0

    def __init__(self, make, model, color, year, narh):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = narh
        Avto.__num_avto += 1

    def __gt__(self, other):
        """True-- > (Katta), False-- < (Kichik)"""
        return self.price > other.price

    def __eq__(self, other):
        """True-- == (Teng), False-- != (Teng emas)"""
        return self.price == other.price

    def __ge__(self, other):
        """True-->= (Katta yoki teng), False--<= (Kichik yoki teng)"""
        return self.price >= other.price

    def __repr__(self):
        return (f"Avto: {self.color} {self.make} {self.model}")


avto1 = Avto("GM", "Malibu", "Qora", 2022, 455_000_000)
avto2 = Avto("GM", "Equinox", "Ko'k", 2023, 485_000_000)
avto3 = Avto("GM", "Monza", "Yashil", 2023, 235_600_000)
avto4 = Avto("GM", "Taxoe", "Oq", 2022, 1_550_000_000)
avto5 = Avto("GM", "Gentra", "Qora", 2021, 190_000_000)
avto6 = Avto("GM", "Onix", "Kulrang", 2023, 201_000_000)


# print(avto1 > avto2)
# print(avto1 < avto2)
# print(avto1 >= avto2)
# print(avto1 <= avto2)
# print(avto1 == avto2)
# print(avto1 != avto2)


class AvtoSalon:
    """AvtoSalon klassi"""
    def __init__(self, name):
        self.name = name
        self.avto_soni = []

    def __repr__(self):
        return f"{self.name} avtosaloni"

    def __len__(self): # avtolar soni bilish
        return len(self.avto_soni)

    def __getitem__(self, item): # kesib olish
        return self.avto_soni[item]

    def __setitem__(self, key, value): # qiymatni o'zgartirish
        if isinstance(value, Avto):
            self.avto_soni[key] = value

    def add_avto(self, *other): # avto qo'shish
        for avto in other:
            if isinstance(avto, Avto):
                self.avto_soni.append(avto)
            else:
                print("Avto obyektini kiriting!")

    def __add__(self, other):
        if isinstance(other, AvtoSalon):
            yangi_salon = AvtoSalon(f"{other.name} {self.name}") # yangi salon yaratish
            yangi_salon.avto_soni = (self.avto_soni + other.avto_soni) # unga avtolar qo'shish

            return yangi_salon # yangi salonni qaytarish

        elif isinstance(other, Avto): # salonga avto qo'shish tayyor metoddan foydalanib
            self.add_avto(other)

        else:
            print(f"AvtoSalon ga {type(other)} qiymat qo'shib bo'lmaydi.")


# avtosalon1 = AvtoSalon("UzDaewoo")
# avtosalon2 = AvtoSalon("Sardor")
#
# avtosalon1.add_avto(avto1, avto2, avto3)
# avtosalon2.add_avto(avto4, avto5, avto6)
# print(len(avtosalon1))

# print(avtosalon1[:2]) # getitem uchun

# avtosalon1[0] = avto3 # setitem uchun
# print(avtosalon1[0])

# avtosalon3 = avtosalon1 + avtosalon2
# print(avtosalon3)
# avtosalon2 + avto3
# print(avtosalon2[:])
