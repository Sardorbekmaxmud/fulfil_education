# ---------------- classwork ---------------------------
# class Person:
#     def __init__(self, name, age, gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
#     def speak(self, word):
#         return f"{self.name} speak: {word}"
#
#
# doe = Person("Doe", 20, 'male')
# anna = Person("Anna", 17, 'female')


# print(doe.speak('Excuse me, Where do you live?'))


# class Person:
#     def __init__(self, name, age, gender):  # konstruktor
#         self.name = name  # atribut
#         self.age = age  # atribut
#         self.gender = gender  # atribut
#
#     def speak(self, work):  # metod
#         return f"{self.name} aytadi: {work}"
#
#
# Doe = Person("Doe", 18, "male")  # Instantiate object
# Ann = Person("Ann", 20, "female")  # Instantiate object


# class Mashina:
#     def __init__(self, name, year, price):
#         self.name = name
#         self.year = year
#         self.price = price
#
#     def speak(self, sound):
#         return f"{self.name.title()}, {sound}"


# bmw = Mashina('bmw x6', 2023, 126000)


# print(bmw.speak('beep'))

# ---------------------- homework ---------------
# # 1
# class Oson1:
#     a = 1
#
#     def outout_a(self):
#         print(self.a)
#
#
# # Oson1.outout_a(Oson1)
#
# class Oson2:
#     a = 2
#     b = 1
#
#     def summa(self):
#         print(self.a + self.b)
#
#
# # Oson2.summa(Oson2)
#
# class Oson3:
#     a = 2
#
#     def plus_minus(self):
#         if self.a >= 0:
#             print('musbat')
#         else:
#             print('manfiy')
#
#
# # print(Oson3.a)
# # Oson3.a = -8
# # print(Oson3.a)
#
# # Oson3.plus_minus(Oson3)
#
# class Oson4:
#     a = 5
#
#     def odd_even(self):
#         if self.a % 2 == 0:
#             print('juft')
#         else:
#             print('toq')
#
#
# # Oson4.odd_even(Oson4)
# # # Oson4.a = 12
# # # Oson4.odd_even(Oson4)
#
# class Oson5:
#     a = 6
#     b = 3
#
#     def daraja(self):
#         print(self.a ** self.b)
#
#
# # Oson5.daraja(Oson5)
#
# class MyClass6:
#     words = []
#
#     def add_word(self, word):
#         self.words.append(word)
#
#     def remove(self, word):
#         try:
#             self.words.remove(word)
#         except:
#             raise "Bundan so'z yo'q"
#
#
# # MyClass6.add_word(MyClass6,'apple')
# # MyClass6.add_word(MyClass6,'phone')
# # MyClass6.add_word(MyClass6,'glass')
# # MyClass6.add_word(MyClass6,'ice-cream')
# # MyClass6.add_word(MyClass6,'pen')
# # MyClass6.add_word(MyClass6,'egg')
# # print(MyClass6.words)
# # MyClass6.remove(MyClass6,'glass')
# # MyClass6.remove(MyClass6,'pin')
#
# # print(MyClass6.words)
#
# class MyClass7:
#     myDict = {}
#
#     def add_elem(self, key, val):
#         if key not in self.myDict.keys():
#             self.myDict[key] = val
#
#     def update_elem(self, key, val):
#         if key in self.myDict.keys():
#             self.myDict.update({key: val})
#
#
# # MyClass7.add_elem(MyClass7,'apple',9)
# # MyClass7.add_elem(MyClass7,'banana',12)
# # MyClass7.add_elem(MyClass7,'pineapple',25)
# # MyClass7.add_elem(MyClass7,'watermelon',47)
# # MyClass7.add_elem(MyClass7,'apple',47)
# # print(MyClass7.myDict)
# # MyClass7.update_elem(MyClass7,'banana',10)
# # print(MyClass7.myDict)
#
# class MyClass8:
#     numbers = [3, 2, 5, 7, 2, 7, 8, 24]
#
#     def compare_list(self, new_list):
#         if sum(self.numbers) > sum(new_list):
#             print(f"numbers --> {self.numbers}", {sum(self.numbers)})
#         else:
#             print(f"new_list --> {new_list}", {sum(new_list)})
#
#
# # MyClass8.compare_list(MyClass8,[23,4,2,8,2,6,1,18])
# # MyClass8.numbers = [243345,45,245]
# # MyClass8.compare_list(MyClass8,[23,4,2,8,2,6,1,18])
#
# class MyClass9:
#     list1 = [4, 6, 13, 7, 55, 1, 68, 47, 2]
#     list2 = [89, 7, 8, 6, 3, 7, 52, 5, 66]
#
#     def list1_max(self):
#         return max(self.list1)
#
#     def list2_max(self):
#         return max(self.list2)
#
#     def sum_of_two_max(self):
#         print(self.list1_max(MyClass9) + self.list2_max(MyClass9))

# print(MyClass9.list1_max(MyClass9))
# print(MyClass9.list2_max(MyClass9))
# MyClass9.sum_of_two_max(MyClass9)


# class MyClass10:
#     numbers = [4, 5, 2, 55, 8, 56, 24, 1, 80, 3, 67]
#
#     def divide(self, d):
#         divisive = []
#
#         for i in self.numbers:
#             if i % d == 0:
#                 divisive.append(i)
#         return divisive


# print(MyClass10.divide(MyClass10, 5))


##-=-=--==-=-=-=-=-=-=-=-Homework f-18 and f-31 groups-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=
# #Oson1. "Oson1" nomli klass elon qiling. Bu klassda "a" integer o'zgaruvchi bor.
# output_a() - bu funksiya klassdagi "a" ni qiymatini print qilsin.

# class Oson1:
#     a = 5
#
#     def output_a(self):
#         print(self.a)
#
#
# Oson1.output_a(Oson1)

# #Oson2. "Oson2" nomli klass elon qililar. Bu klassda "a" va "b" integer o'zgaruvchilari bor.
# summa() - bu funksiya klassdagi "a" va "b" ni yig'indisini print qilsin.
# class Oson2:
#     a = 4
#     b = 7
#
#     def summa(self):
#         print(self.a + self.b)
#
#
# Oson2.summa(Oson2)

# #Oson3. "Oson3" nomli klass elon qililar. Bu klassda "a" integer o'zgaruvchisi bor.
# plus_minus() - bu funksiya klassdagi "a" ni musbat yoki manfiy ekanligini print qilsin.
# class Oson3:
#     a = 6
#
#     def plus_minus(self):
#         print("musbat" if self.a > 0 else "manfiy" if self.a < 0 else "teng")
#
#
# Oson3.plus_minus(Oson3)
# Oson3.a = -6
# Oson3.plus_minus(Oson3)
# Oson3.a = 0
# Oson3.plus_minus(Oson3)


# #Oson4. "Oson4" nomli klass elon qililar. Bu klassda "a" integer o'zgaruvchi bor.
# odd_even() - bu funksiya klassdagi "a" ni toq yoki juft ekanligini print qilib bersin.
# class Oson4:
#     a = 5
#
#     def odd_even(self):
#         print("juft" if self.a % 2 == 0 else "toq")
#
#
# Oson4.odd_even(Oson4)
# Oson4.a = 12
# Oson4.odd_even(Oson4)


# #Oson5. "Oson5" nomli klass elon qililar. Bu klassda "a" va "b" integer o'zgaruvchisi bor.
# daraja() - bu funksiya klassdagi "a" ni "b" chi darajasini print qilsin.
# class Oson5:
#     a = 5
#     b = 3
#
#     def odd_even(self):
#         print(self.a ** self.b)
#
#
# Oson5.odd_even(Oson5)


# #MyClass1 nomli klass elon qililar. with_max(a, b) funksiya yozinglar
# a va b sonlaridan qaysi biri katta bo'lsa shuni print qilsin.
# class MyClass1:
#     def with_max(self, a, b):
#         print(f"a = {a}" if a > b else f"b = {b}" if b > a else "ular teng")
#
#
# MyClass1.with_max(MyClass1, 23, 14)
# MyClass1.with_max(MyClass1, 23, 34)
# MyClass1.with_max(MyClass1, 34, 34)

# #MyClass2 nomli klass e'lon qilinglar. odd_or_even(num) funksiya yozinglar
# u num toq yoki juft ekanligini print qilsin.
# class MyClass2:
#     def odd_or_even(self, num):
#         print("juft" if num % 2 == 0 else "toq")
#
#
# MyClass2.odd_or_even(MyClass2, 5)
# MyClass2.odd_or_even(MyClass2, 8)


# #MyClass3 nomli klass e'lon qilinglar. reverse(word) funksiyasi ichida bo'lsin
#  U kelyotgan wordni teskari qilib return qilsin javobni pastda print qiling!
# class MyClass3:
#     def reverse(self, word):
#         return word[::-1]
#
#
# print(MyClass3.reverse(MyClass3, "word"))
# print(MyClass3.reverse(MyClass3, "drow"))


# #MyClass4 nomli klass e'lon qilinglar.
# class MyClass4:
#     def find_more_letter(self, word1, word2, letter):
#         word1_count = word1.count(letter)
#         word2_count = word2.count(letter)
#         if word1_count > word2_count:
#             return word1
#         if word1_count < word2_count:
#             return word2
#         else:
#             return "teng"
#
#
# print(MyClass4.find_more_letter(MyClass4, "annajohn", "jekronild", "k"))


# #MyClass5 nomli klass e'lon qilinglar.
# class MyClass5:
#     number_list = []
#
#     def add_elem(self, a):
#         self.number_list.append(a)
#
#     def get_max_elem(self):
#         return max(self.number_list)
#
#     def get_min_elem(self):
#         return min(self.number_list)
#
#
# MyClass5.add_elem(MyClass5, 5)# add elem
# MyClass5.add_elem(MyClass5, 23)# add elem
# MyClass5.add_elem(MyClass5, 43)# add elem
# MyClass5.add_elem(MyClass5, 87)# add elem
# MyClass5.add_elem(MyClass5, 1)# add elem
#
# print(MyClass5.get_max_elem(MyClass5))
# print(MyClass5.get_min_elem(MyClass5))


# #"MyClass6" nomli klass elon qililar. Bu klassda "words" list bo'sh o'zgaruvchisi bor.
# add_word(word) - bu funksiya "words" ga element qo'shib qo'ysin.
# remove(word) = bu funksiya "words" da "word" ni o'chirib tashlasin.
# class MyClass6:
#     words = []
#
#     def add_word(self, word):
#         self.words.append(word)
#
#     def remove_word(self, word):
#         if word in self.words:
#             self.words.remove(word)
#         else:
#             print("Bunday so'z mavjud emas!")
#
#
# MyClass6.add_word(MyClass6, "banana")
# MyClass6.add_word(MyClass6, "apple")
# MyClass6.add_word(MyClass6, "chery")
# MyClass6.remove_word(MyClass6, "apple")
#
# print(MyClass6.words)


# #"MyClass7" nomli klass elon qiling. Bu klassda bo'sh "myDict" dictionary o'zgaruvchisi bor.
# add_elem(key, val) - bu funksiya "myDict" "key" ni qiymatiga teng bo'lgan key bo'lmasa "val" ni add qilsin,
# bor bolsa xech narsa qilmasin.
# update_elem(key, val) - bu funksiya "myDict" shu "key" ni qiymatiga teng bolgan key bo'lsa "val" ni update qilsin,
# yoq bolsa xech narsa qilmasin.
# class MyClass7:
#     myDict = {}
#
#     def add_elem(self, key, val):
#         if key not in self.myDict.keys():
#             self.myDict[key] = val
#
#     def update_elem(self, key, val):
#         if key in self.myDict.keys():
#             self.myDict.update({key: val})
#
#
# MyClass7.add_elem(MyClass7, "bir_key", "qiymat_val") # yaratish
# MyClass7.add_elem(MyClass7, "bir_key", "qiymat2_val") # uning key i o'zgarmasligini tekshirish
# MyClass7.add_elem(MyClass7, "ikki_key", "qiymat2_val") # yana yangi yaratish
# MyClass7.update_elem(MyClass7, "ikki_key", "yangi_qiymat_val") #uni key bor bo'lsa yangilash
# MyClass7.update_elem(MyClass7, "bir_key2", "yangi_qiymat_val") # key yo'qligini tekshirish
#
# print(MyClass7.myDict)


# #MyClass8 nomli klass e'lon qilinglar.
# class MyClass8:
#     numbers = [6, 7, 7, 3, 7, 8, 46, 6, 3, 42]
#
#     def compare_lists(self, new_list):
#         sum_numbers_list = sum(self.numbers)
#         sum_new_list = sum(new_list)
#
#         if sum_numbers_list > sum_new_list:
#             print("numbers =", self.numbers)
#         else:
#             print("new_list =", new_list)
#
#
# MyClass8.compare_lists(MyClass8, [4, 6, 7, 22, 7, 8, 0])
# MyClass8.numbers = [0, 2, 2, 6, 4, 5, 3, 3]
# MyClass8.compare_lists(MyClass8, [4, 6, 7, 22, 7, 8, 0])


# #MyClass9 nomli klass e'lon qilinglar.
# class MyClass9:
#     list1 = [5, 7, 2, 3, 7]
#     list2 = [9, 3, 3, 6]
#
#     def list1_max(self):
#         return max(self.list1)
#
#     def list2_max(self):
#         return max(self.list2)
#
#     def sum_of_two_max(self):
#         print(self.list1_max(MyClass9) + self.list2_max(MyClass9))
#
#
# print(MyClass9.list1_max(MyClass9))
# print(MyClass9.list2_max(MyClass9))
# MyClass9.sum_of_two_max(MyClass9)


# #MyClass10 nomli klass e'lon qilinglar.
# class MyClass10:
#     numbers = [6, 7, 7, 3, 7, 8, 46, 6, 3, 42]
#
#     def divide(self, d):
#         return [i for i in self.numbers if i % d == 0]
#
#
# print(MyClass10.divide(MyClass10, 6))


# #Vorisdorlik-1
# class Texnika:
#     def __init__(self, brand, model, type_):
#         self.brand = brand
#         self.model = model
#         self.types = type_
#
#     def info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.types}")
#
#
# class Notebooks(Texnika):
#     def __init__(self, brand, model, type_, video_card, ram, display):
#         super().__init__(brand, model, type_)
#         self.video_card = video_card
#         self.ram = ram
#         self.display = display
#
#     def more_info(self):
#         print(
#             f"Brand: {self.brand}, Model: {self.model}, Type: {self.types}, Video card: {self.video_card}, RAM: {self.ram}, Display: {self.display}")
#
#
# class Televisions(Texnika):
#     def __init__(self, brand, model, type_, size, display):
#         super().__init__(brand, model, type_)
#         self.size = size
#         self.display = display
#
#     def more_info(self):
#         print(
#             f"Brand: {self.brand}, Model: {self.model}, Type: {self.types}, Size: {self.size}, Display: {self.display}")
#
#
# class Smartphones(Texnika):
#     def __init__(self, brand, model, type_, size, sim_count):
#         super().__init__(brand, model, type_)
#         self.size = size
#         self.sim_count = sim_count
#
#     def more_info(self):
#         print(
#             f"Brand: {self.brand}, Model: {self.model}, Type: {self.types}, Size: {self.size}, SIM Count: {self.sim_count}")


# tex1 = Texnika("LG", "4k television", "43 Full LED")
# tex1.info()

# laptop1 = Notebooks("HP", "Victus 15", "Simple", "NVIDIA GTX 1650 4GB", "8GB", "Simple display 144Hz")
# laptop1.info()
# laptop1.more_info()

# televi1 = Televisions("Artel", "Artel 4k", "None", "43", "Full HD")
# televi1.info()
# televi1.more_info()

# phone1 = Smartphones("Artel", "Tomchi", "Simple", 5.6, 2)
# phone1.info()
# phone1.more_info()


# #Vorisdorlik-2
# class Transport:
#     def __init__(self, brand, model, type_):
#         self.brand = brand
#         self.model = model
#         self.type = type_
#
#     def info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}")
#
#
# class ElentroCars(Transport):
#     def __init__(self, brand, model, type_, battery_life, chargin_time):
#         super().__init__(brand, model, type_)
#         self.battery_life = battery_life
#         self.chargin_time = chargin_time
#
#     def more_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, Battery Life: {self.battery_life}, Chargin time: {self.chargin_time}")
#
#
# class SportCars(Transport):
#     def __init__(self, brand, model, type_, motor, color):
#         super().__init__(brand, model, type_)
#         self.motor = motor
#         self.color = color
#
#     def more_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, Motor: {self.motor}, Color: {self.color}")
#
# class Truck(Transport):
#     def __init__(self, brand, model, type_, motor, height, long, weight):
#         super().__init__(brand, model, type_)
#         self.motor = motor
#         self.height = height
#         self.long = long
#         self.weight = weight
#
#     def more_info(self):
#         print(f"Brand: {self.brand}, Model: {self.model}, Type: {self.type}, Motor: {self.motor} hp, Height: {self.height} sm, Long: {self.long} sm, Weight: {self.weight} kg")


# trans1 = Transport("Bugatti", "Cheyron", "Sedan")
# trans1.info()

# elect_car1 = ElentroCars("Tesla", "Model 3", "Sedan", 150_000, "2 hours")
# elect_car1.info()
# elect_car1.more_info()

# sp_car1 = SportCars("BMW", "M5 Competation", "Sedan", 5, "black")
# sp_car1.info()
# sp_car1.more_info()

# truck1 = Truck("Volvo", "FH", "truck", "380-540", 171, 6585, 5080)
# truck1.info()
# truck1.more_info()


