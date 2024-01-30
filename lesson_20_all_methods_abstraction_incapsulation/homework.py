# # 1
# class BankAccount:
#     def __init__(self, balance: int):
#         self.__balance = balance
#
#     def deposit(self, add_money: int):
#         self.__balance += add_money
#         print("Muvaffaqiyatli pul qo'shildi!")
#
#     def withdraw(self, sub_money):
#         self.__balance -= sub_money
#         print("Balansingizdan {:_} yechildi.".format(sub_money))
#
#     def check_balance(self):
#         print("Balansingiz: {:_} so'm".format(self.__balance))
#
#
# user1 = BankAccount(balance=23_534_998)
# user1.check_balance()
# user1.deposit(add_money=1_200_000)
# user1.deposit(add_money=13_500_000)
# user1.check_balance()
# user1.withdraw(sub_money=3_000_000)
# user1.check_balance()


# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def area(self):
#         print("Yuzasi:",self.length * self.width)
#
#     def parimetr(self):
#         print("Parimetr:",2 * (self.length + self.width))
#
#     def is_square(self):
#         if self.length == self.width:
#             print("Yes, it's square")
#         else:
#             print("No, It's not square")
#
#
# square1 = Rectangle(5, 5)
# square1.area()
# square1.parimetr()
# square1.is_square()

# # 3
# class Student:
#     def __init__(self, name: str, age: int, grades: list):
#         self.name = name
#         self._age = age
#         self._grades = grades
#
#     def add_grades(self, add_grade: int):
#         self._grades.append(add_grade)
#
#     def calculate_average(self):
#         try:
#             result = sum(self._grades)/len(self._grades)
#             return result
#         except:
#             print("Bahosi yo'q")
#             return
#
#     def print_summary(self):
#         result = self.calculate_average()
#         if result == None:
#             pass
#         elif result>=4.5:
#             print(f"Talaba {self.name} fakultetning eng oldi o'quvchilarimizdan!")
#         elif result>=3.5:
#             print(f"Talaba {self.name} o'qishlari yaxshi.Harakat qilsa bundan-da yaxshi bo'lib ketadi.")
#         else:
#             print(f"Talaba {self.name} shu ketishda o'qisa o'qishdan haydaladi.")
#
#
# stud = Student("Akbar", 21, [])
# stud.add_grades(add_grade=4)
# stud.add_grades(add_grade=3)
# stud.add_grades(add_grade=5)
# stud.add_grades(add_grade=4)
# stud.add_grades(add_grade=5)
# print(stud.calculate_average())
# stud.print_summary()

# #4
# import math

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return "Yuzasi: {:f}".format(math.pi * self.radius ** 2)
#
#     def circumference(self):
#         return "Aylana uzunligi: {:f}".format(2 * math.pi * self.radius)
#
#     def diameter(self):
#         return f"Diametri: {2 * self.radius}"
#
#
# circle = Circle(4)
# print(circle.area())
# print(circle.circumference())
# print(circle.diameter())

# #5
# class Book:
#     def __init__(self, title: str, author: str, current_page: int):
#         self.title = title
#         self.author = author
#         self.current_page = current_page
#
#     def open(self, page_number):
#         self.current_page = page_number
#         print(f"Open {self.current_page} page.")
#
#     def turn_page(self):
#         self.current_page += 1
#         print(f"Open next {self.current_page} page")
#
#     def restart(self):
#         self.current_page = 1
#
#
# book1 = Book("Amallar niyatga bog'liqdir", "Shayx Muhammad Sodiq Muhammad Yusuf", 1)
# book1.open(3)
# book1.restart()
# book1.turn_page()
# book1.open(56)
# book1.turn_page()

##class method tasks-=--=====-------====----------======-=-
# #6
# class Dog:
#     total_dogs = 0
#
#     @classmethod
#     def get_total_dogs(cls):
#         return f"The number of dogs: {cls.total_dogs}"
#
#
# Dog.total_dogs += 1
# Dog.total_dogs += 1
# Dog.total_dogs += 1
# Dog.total_dogs += 1
# Dog.total_dogs += 1
#
# print(Dog.get_total_dogs())


# #7
# class Computer:
#     total_computers = 0
#     computers_list = []
#
#     @classmethod
#     def add_computer(cls, new_comp):
#         cls.total_computers += 1
#         cls.computers_list.append(new_comp)
#
#
# Computer.add_computer("MacOs")
# Computer.add_computer("HP Victus 15")
# Computer.add_computer("Lenovo")
# Computer.add_computer("Asus")
# print("List of computers:",Computer.computers_list)
# print("Number of computers:",Computer.total_computers)


# #8
# class Employee:
#     total_employees = 0
#     employees_list = []
#
#     @classmethod
#     def hire_employee(cls, new_employee):
#         cls.total_employees += 1
#         cls.employees_list.append(new_employee)
#
#
# Employee.hire_employee("Jonson")
# Employee.hire_employee("Jenna")
# Employee.hire_employee("Georgio")
# Employee.hire_employee("Klark")
# Employee.hire_employee("Doe")
# Employee.hire_employee("Boris")
#
# print("List of employees:", Employee.employees_list)
# print("Number of employees:", Employee.total_employees)


# #9
# class Television:
#     average_screen = 0
#
#     @classmethod
#     def update_average_screen(cls, new_television: int):
#         cls.average_screen = new_television
#
#
# Television.update_average_screen(24)
# print("Size of television:",Television.average_screen)
# Television.update_average_screen(42)
# print("Size of television:",Television.average_screen)
# Television.update_average_screen(55)
# print("Size of television:",Television.average_screen)


# #10
# class Course:
#     total_courses = 0
#     courses_list = []
#
#     @classmethod
#     def add_courses(cls, new_cours):
#         cls.total_courses += 1
#         cls.courses_list.append(new_cours)
#
#
# Course.add_courses("Python Backend")
# Course.add_courses("React JS Frontend")
# Course.add_courses("Node JS Backend")
# Course.add_courses("Data Science")
# print("List of courses:", Course.courses_list)
# print("Number of courses:", Course.total_courses)


## Static method tasks-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# #11
# class Math:
#     @staticmethod
#     def multiply(x, y):
#         return f"{x} * {y} = {x * y}"
#
#
# print(Math.multiply(2, 3))


# #12
# class Temperature:
#     @staticmethod
#     def celsius_to_fahrenheit(celsius):
#         return f"{celsius}°C = {celsius * 1.8 + 32}°F"
#
#
# print(Temperature.celsius_to_fahrenheit(34))


# #13
# class Distance:
#     @staticmethod
#     def miles_to_kilometers(mile):
#         return f"Mile {mile} = {mile * 1.609344} Kilometre"
#
#
# print(Distance.miles_to_kilometers(7))


# #14
# class Utility:
#     @staticmethod
#     def is_even(even):
#         return "even" if even % 2 == 0 else "not even"
#
#
# print(Utility.is_even(7))
# print(Utility.is_even(2))
# print(Utility.is_even(136))
# print(Utility.is_even(123))


# class Time:
#     @staticmethod
#     def seconds_to_minutes(secund):
#         return "Secund:",secund,"Minute:",secund // 60
#
#
# print(Time.seconds_to_minutes(360))


a = 10
b = 20

a, b = b, a

print("a =", a, "b =", b)
