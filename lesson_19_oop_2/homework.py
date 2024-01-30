# #vorisdorlik oop_2 dagi misollar
# #3.1
#   "University" - parent klass. Konstruktorida esa (university) parametrlari bor.
#     info() - (university) ni print qilib beradi.
#
#   "Staff" - child klass. Unda konstruktirida qo'shimcha (first_name, last_name, age) parametrlari bor.
#     staff_info() - (university, first_name, last_name, age) ni print qilib beradi.
#
#   "Student" - child klass. U "Staff" dan vorislik oladi. Unda konstruktirida qo'shimcha (group) parametrlari bor.
#     more_info() - (university, first_name, last_name, age, group) ni print qilib beradi.
#
#   "Teacher" - child klass. U "Staff" dan vorislik oladi. Unda konstruktirida qo'shimcha (position, subject) parametrlari bor.
#     more_info() - (university, first_name, last_name, position, subject) ni print qilib beradi.
#
#   "OtherStaff" - child klass. U "Staff" dan vorislik oladi. Unda konstruktirida qo'shimcha (position) parametrlari bor.
#     more_info() - (university, first_name, last_name, position,) ni print qilib beradi.

# class University:
#     def __init__(self, university):
#         self.university = university
#
#     def info(self):
#         print(f"University: {self.university}")


# univer1 = University("TATU")
# univer1.info()

# class Staff(University):
#     def __init__(self, university, first_name, last_name, age):
#         super().__init__(university)
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def more_info(self):
#         print(f"University: {self.university}, Ism: {self.first_name}, Familya: {self.last_name}, Age: {self.age}")


# staff1 = Staff("TATU", "Jahongir", "Vohidov", 22)
# staff1.info()
# staff1.more_info()


# class Student(Staff):
#     def __init__(self, university, first_name, last_name, age, group):
#         Staff.__init__(self, university, first_name, last_name, age)
#         self.group = group
#
#     def more_info(self):
#         print(
#             f"University: {self.university}, Ism: {self.first_name}, Familya: {self.last_name}, Age: {self.age}. Group: {self.group}")


# student1 = Student("TATU", "Karim", "Osimov", 20, "Computer science")
# student1.info()
# student1.more_info()


# class Teacher(Staff):
#     def __init__(self, university, first_name, last_name, age, position, subject):
#         Staff.__init__(self, university, first_name, last_name, age)
#         self.position = position
#         self.subject = subject
#
#     def more_info(self):
#         print(
#             f"University: {self.university}, Ism: {self.first_name}, Familya: {self.last_name}, Position: {self.position}, Subject: {self.subject}")
#
#
# teacher1 = Teacher("TATU", "G'iyos", "Dostonov", 35, "domla", "Computer science")
# teacher1.info()
# teacher1.more_info()
#
#
# class OtherStaff(Staff):
#     def __init__(self, univeristy, first_name, last_name, age, position):
#         Staff.__init__(self, univeristy, first_name, last_name, age)
#         self.position = position
#
#     def more_info(self):
#         print(
#             f"University: {self.university}, Ism: {self.first_name}, Familya: {self.last_name}, Position: {self.position}")
#
#
# oth_st1 = OtherStaff("INHA", "Botir", "Olloyorov", 41, "Direktor")
# oth_st1.info()
# oth_st1.more_info()


# #3.2
# "Object" - child klass. U "University" dan vorislik oladi. Unda konstruktirida qo'shimcha (name) parametrlari bor.
#     object_info() - (university, name) ni print qilib beradi.
#
#   "Computer" - child klass. U "Object" dan vorislik oladi. Unda konstruktirida qo'shimcha (soni, tizimi, holati) parametrlari bor.
#     object_more_info() - (university, name, soni, tizimi, holati) ni print qilib beradi.
#
#   "Mebel" - child klass. U "Object" dan vorislik oladi. Unda konstruktirida qo'shimcha (soni, turi, holati) parametrlari bor.
#     object_more_info() - (university, name, soni, turi, holati) ni print qilib beradi.


# class Object(University):
#     # call_count = 0
#
#     def __init__(self, university, name):
#         # Object.call_count += 1
#         super().__init__(university)
#         self.name = name
#
#     def object_info(self):
#         print(f"University: {self.university}, Object name: {self.name}")


# obj1 = Object("New Uzbekistan", "Build")
# obj2 = Object("INHA", "Build")
# obj1.object_info()
## print(Object.call_count)


# class Computer(Object):
#     def __init__(self, university, name, soni, tizimi, holati):
#         super().__init__(university, name)
#         self.count = soni
#         self.system = tizimi
#         self.holati = holati
#
#     def object_more_info(self):
#         print(
#             f"Univerity: {self.university}, Name: {self.name}, Count: {self.count}, System: {self.system},"
#             f" Holati: {self.holati}")

# comp1 = Computer("CHDPI", "Apple", 155, "MacOS", "active")
# comp1.info()
# comp1.object_info()
# comp1.object_more_info()


# class Mebel(Object):
#     def __init__(self, university, name, soni, turi, holati):
#         super().__init__(university, name)
#         self.count = soni
#         self.type = turi
#         self.holati = holati
#
#     def object_more_info(self):
#         print(
#             f"Univerity: {self.university}, Name: {self.name}, Count: {self.count}, Type: {self.type},"
#             f" Holati: {self.holati}")
#
#
# mebel1 = Mebel("AMI", "Table", 530, "Simple", "Good")
# mebel1.info()
# mebel1.object_info()
# mebel1.object_more_info()
