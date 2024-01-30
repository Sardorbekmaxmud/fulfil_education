# class Student:
#     school_name = 'ABC School'  # class attribute
#
#     def __init__(self, name, age):
#         self.name = name  # instance attribute
#         self.age = age  # instance attribute
#
#     @classmethod  # endi classmethod bo'ldi
#     # # cls bu yerda == Student ga teng
#     def change_school(cls, school_name):  # classmethod
#         cls.school_name = school_name  # update class attribute
#
#     def show(self):  # instance method
#         print(self.name, self.age, "School", Student.school_name)


# obyekt yaratish Student klassidan
# jessa = Student('Jessa', 20)
# jessa.show()
#
# # call change_school classmethod
# Student.change_school("XYZ School") #update school_name
# jessa.show()

# from datetime import datetime
#
#
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def calculate_age(cls, name, birth_year):
#         return cls(name, datetime.now().year - birth_year)
#
#     def show(self):
#         print(f"{self.name}'s age is {self.age}")
#
#
# # obyekt yaratish Student klassidan
# georgio = Student(name="Georgio", age=25)
# georgio.show()
#
# # agar mobodo yoshini bilmasa yilini kiritib yangi obyekt
# # yaratish factory metodi yordamida
# jack = Student.calculate_age(name="Jack", birth_year=1996)
# jack.show()


# class Employee:
#     @staticmethod
#     def sample(x):
#         print("Static metod ichi. Parametr:", x)
#
#
# Employee.sample("Hi!")
#
# emp = Employee()
# emp.sample(10)


# class Employee(object):
#     def __init__(self, name, salary, project_name):
#         self.name = name
#         self.salary = salary
#         self.project_name = project_name
#
#     @staticmethod
#     def gather_requirement(project_name):
#         if project_name == "ABC Project":
#             requirement = ['task1', "task2", "task3"]
#         else:
#             requirement = ['task1']
#         return requirement
#
#     def work(self):
#         requirement = self.gather_requirement(self.project_name)
#         for task in requirement:
#             print("Completed", task)
#
#
# emp = Employee("Komiljon", 5000, "Inside Beeline Project")
# emp2 = Employee("Jack", 9500, "ABC Project")
# emp.work()
# emp2.work()

# class Test:
#     @staticmethod
#     def static_method_1():
#         print("static method 1")
#
#     @staticmethod
#     def static_method_2():
#         Test.static_method_1()
#
#     @classmethod
#     def class_method_1(cls):
#         cls.static_method_2()
#
#
# Test.class_method_1()


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.__salary = salary
# self.project = project

# def show(self):
#     print("Name:", self.name, "Salary:", self.salary)

# def work(self):
#     print(self.name, "is working on", self.project)


# emp = Employee("Jack", 9400) #"NLP"
# print(emp.name)
# print(emp._Employee__salary)

# print("Name:", emp.name, "Salary:", emp.salary)
# emp.show()
# emp.work()


# class Company:
#     def __init__(self):
#         # protected data member
#         self._project = "NLP"
#
#
# class Employee(Company):
#     def __init__(self, name):
#         # public data member
#         self.name = name
#         # call Parent class constructor
#         Company.__init__(self)
#
#     def show(self):
#         print("Xodim ismi:", self.name)
#         print("Ishlayotgan proyekti:", self._project)
#
#
# emp = Employee("Jack")
# emp.show()
#
# print("Project:", emp._project)


# class Student:
#     def __init__(self, name, age):
#         self.name = name # public method
#         self.__age = age # private method
#
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, age):
#         self.__age = age
#
#
# student = Student("Akmal", 23)
# print("Name:", student.name, student.get_age())
#
# student.set_age(24)
# print("Name:", student.name, student.get_age())


# class Student:
#     def __init__(self, name, roll_no, age):
#         self.name = name # public variable
#         self.__roll_no = roll_no # private variable
#         self.__age = age # private variable
#
#
#     def show(self):
#         print("Student Details:", self.name, self.__roll_no)
#
#     def get_roll_no(self):
#         return self.__roll_no
#
#     def set_roll_no(self, number):
#         if number > 50:
#             print("Xato rulon raqami. Iltimos to'g'ri rulon raqamini kiriting!")
#         else:
#             self.__roll_no = number
#
#
# georgio = Student("Georgio", 7, 22)
# georgio.show()
#
# # print(georgio.get_roll_no())
#
# georgio.set_roll_no(51)
#
# georgio.set_roll_no(31)
# georgio.show()
