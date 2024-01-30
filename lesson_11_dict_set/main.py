# dict homework
# from collections import Counter


# from copy import deepcopy

from collections import Counter

str_counter = (["shaftoli", "olma", "nok", ])

counter = Counter(str_counter)
print(counter)

# # 1
from collections import Counter


def str_counter(str_list):
    counter_str = dict(Counter(str_list))
    return counter_str


print(str_counter(["shaftoli", "olma", "nok"]))

# # 2
# def merge_list(l1,l2):
#     d = {}
#     for i in range(len(l1)):
#         d[l1[i]]=l2[i]
#     return d

# list_1 = ["a", "b", "c"]
# list_2 = [1, 2, 3]
# print(merge_list(list_1,list_2))

# # 3
# contacts = {"Nodir":"+998918602711", "Laziz":"+998908002534"}

# while True:
#     print("""
#     ➕ Added  Contact --> 1
#     ♻️  Update contact --> 2
#     ✅ All contacts   --> 3
#     🗑️  Delete contact --> 4
#     🔍 Search contact --> 5
#     🔚 Exit           --> 0""")

#     amal = input("Amallarni tanlang: ")

#     if amal=="1":
#         ism=input('Ism: ')
#         raqam=input('Raqam: ')
#         contacts[ism]=raqam
#         print("Added contact")

#     elif amal=="2":
#         ism=input('Ism: ')
#         raqam=input('Raqam: ')
#         contacts.update({ism:raqam})
#         print("Update contact")

#     elif amal=='3':
#         print(contacts)

#     elif amal=="4":
#         ism=input("Ism: ")
#         if contacts.get(ism):
#             del contacts[ism]
#             print("deleted contact")
#         else:
#             print("bunday kontakt yo'q")

#     elif amal=="5":
#         ism=input("Ism: ")
#         if contacts.get(ism):
#             print(contacts[ism])
#         else:
#             print("bunday kontakt yo'q")

#     elif amal=="0":
#         break

#     else:
#         print("Siz boshqa amalni tanladingiz!")
#         continue

# # 4
# def counter_dict(nums):
#     d = dict(Counter(nums))
#     return d

# print(counter_dict([2,1,1,1]))
# print(counter_dict([2,1,"w","r","r",1,1,"w","a","w",True,False,0,1,False,-1,"-1","-1"]))

# # 5
# def max_ball_students(talabalar):
#     t1_k = max(talabalar, key=talabalar.get)
#     t1_v = talabalar[t1_k]
#     del talabalar[t1_k]
#     t2_k = max(talabalar,key=talabalar.get)
#     return dict([[t1_k,t1_v],[t2_k,talabalar[t2_k]]])

# print(max_ball_students({"Akmal":64, "Tohir":55, "Nodir":76, "Zafar":80,}))


# ==================================DICT METODS===================================================
# # 1
# car = {
#     'name':"mustang",
#     'year':2020,
#     'price':45_000
# }
# print(car)

# car.clear()
# print(car)

# # 2
# prog_lang = {
#     "python":{"name":["python","1989"]},
#     "c":{'name':"c"},
#     "java":{"name":"java"}
# }
# copy_dict1 = prog_lang.copy()
# copy_dict2 = deepcopy(prog_lang)
# copy_dict1['python']['name'][0] = 'Python'
# copy_dict2['python']['name'][0] = 'Python'
# print(prog_lang)
# print(copy_dict1)
# print(copy_dict2)

# # 3
# s = {'kalit','kalit2','kalit3','kalit4','kalit5'}
# d = dict.fromkeys(s) # default qiymat None
# d2 = dict.fromkeys(s,True) # qo'lda bersa ham bo'ladi
# print(d)
# print(d2)

# # 4
# dict1 = {'car':2,'house':3,'cat':"1"}
# print(dict1.get('car'))
# print(dict1.get('phone',1)) # agar key bo'lmasa qiymat berib ketsak bo'ladi

# # 5
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x=car.items()

# print(x)
# car['year']=2012 # items metodidan keyin dict ni o'zgartirsang items dagi ham o'zgaradi
# print(x)

# # 6
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# keys_car = car.keys()

# print(keys_car)
# car['color']='white' # keys da ham shunday dict da o'zgarish bo'lsa ham qo'shilib qoladi
# print(keys_car)

# # 7
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# values_car = car.values()

# print(values_car)
# car['year']=2022 # values da ham shunday dict da o'zgarish bo'lsa ham qo'shilib qoladi
# car['color']='white' # values da ham shunday dict da o'zgarish bo'lsa ham qo'shilib qoladi
# print(values_car)

# # 8
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.pop('brand')
# print(car) # dict
# print(x) # pop faqat values i ni oladi

# # 9
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.popitem() # to'liq oladi key:value default oxirgisini oladi
# print(car)
# print(x)

# # 10
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(car)
# x = car.setdefault('brand')
# c = car.setdefault('color','black') # bu dict da bu key bo'lmas o'zi qo'shib ketadi
# print(x)
# print(c)
# print(car)

# # 11
# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# print(car)
# car.update({"color":"blue"})
# print(car)

# car = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }

# add_dict = {
#     ("color",'black'),
#     ('company','Ford Cor')
# }
# print(type(add_dict))
# car.update([('a', 1)])
# print(car)


# ===================================SET METODS===================================================
# # add bu set ga yangi element qo'shish
# fruits = {'apple','orange'}
# fruits.add('pear')
# print(fruits)

# # set ni tozalash
# fruits = {'orange', 'apple', 'pear'}
# fruits.clear()
# print(fruits)

# # listni copy qilish
# car = {'bmw','hyundai','kia','mitsubishi'}
# new_car = car.copy()
# print(new_car)

# # bu metod 1-setdagi ma'lumot 2-setda yo'qlarini oladi va yangi set ochadi
# car = {'mers','audi','lamburgino'}
# add_car = {'bmw','volvo','mers'}

# d = car.difference(add_car)
# # print(car)
# print(d)

# # bu metod asl listni o'zgartiradi
# car = {'mers','audi','lamburgino'}
# add_car = {'bmw','volvo','mers'}

# # print(id(car))
# car.difference_update(add_car)
# print(car)

# # discard o'chirish metodi bunda xato qaytarmaydi
# names = {'karim','laylo',"ulug'bek"}
# names.discard('karim')
# print(names)

# # intersection bu metod 1-setdagi element 2-setda borlarini yangi setga oladi
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# a = x.intersection(y)
# print(a)

# # bu yangi setni ochmaydi qaysi setdan foydalansa o'shani o'zgartiradi
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# x.intersection_update(y)
# print(x)

# # isdisjoint bu 1 setdagi 2 setda bo'lmasa true qaytaradi bo'lsa false
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}

# z = x.isdisjoint(y)
# print(z)

# # y setidagi elementlar x da bo'lsa true qaytaradi yoki false
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "banana", "cherry",'apple'}

# a = {"apple", "banana", "cherry"}
# b = {"google", "microsoft",'apple'}

# z = a.issubset(b)
# print(z)

# # x setdagi elementlar y da bo'lsa true bo'lmasa false qaytaradi
# x = {"apple", "banana", "cherry",'google','microsoft'}
# y = {"google", "microsoft"}

# a = {"apple", "banana", "cherry"}
# b = {"google", "microsoft",'apple'}

# z = x.issuperset(y)
# print(z)
# z = a.issuperset(b)
# print(z)

# # pop() metodi set dan elementni sug'urib oladi random tarzida
# x = {"apple", "banana", "cherry",'pear','orange'}
# meva = x.pop()
# print(meva)

# # remove o'chiradi faqat nomalumni o'chir kerak bo'lib qolsa xato qaytaradi
# x = {"apple", "banana", "cherry",'pear','orange'}
# x.remove('apple')
# print(x)

# # setlarni qo'shadi xoxlagancha
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# d = {"google1", "micros1oft", "app1le"}

# z = x.union(y,d)
# print(z)

# # setni yangilash xoxlagancha argument bersa bo'ladi faqat list,tuple,serda bo'lishi kerak
# x = {"apple", "banana", "cherry"}
# y = ("google", "microsoft", "apple")

# x.update(y)
# print(x)
# z = x.update(y) # o'zgaruvchiga yuklab bo'lmaydi None yuklasa ham Nond ga teng
# z.add('a')
# print(id(x))
# print(z)
# print(id(z))

# # bu metod cardagi va car2 dagi elementlarni yo'qlarni tanlab yangi setga yuklaydi asl o'zgarmay qoladi
# car = {'toyota','mers','audi','lamburgino'}
# car2 = {'bmw','rolls roys','mers','nissan'}
# all_cars = car.symmetric_difference(car2)
# print(all_cars)

# # bu metod cardagi va car2 dagi elementlarni yo'qlarni tanlab asl setni o'zgartiradi
# car = {'toyota','mers','audi','lamburgino'}
# car2 = {'bmw','rolls roys','mers','nissan'}
# car.symmetric_difference_update(car2)
# print(car)

# #-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-==--==-QAYTA YECHIM=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=
# a = [1, 2, 3, [4, 5]]
# b = a[:]
# c = a.copy()
# d = a
# print(id(a),id(b),id(c),id(d))
# b[3].append(6)
# print(a)

# # 1 -=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-===-=-=-=-=-=-=----=-=-=--=----=--=--=-=-==-=-=
# from collections import Counter
# from copy import deepcopy

# def str_counter(strs):
#     """Funksiya listni qabul qilib uni ichidagi strlarni soni va o'zini dict ga solib qaytaradi"""
#     dict_len_str = {}
#     for i in strs:
#         dict_len_str[len(i)] = i
#     return dict_len_str

# print(str_counter(['shaftoli', 'olma', 'nok']))
# # 2
# def merge_list(l1, l2):
#     """2 ta list qabul qilib, 1-listni kalit, 2-listni qiymat qilib dict ko'rinishida qaytaruvchi funksiya"""
#     d = {}
#     for i in range(len(l1)):
#         d[l1[i]] = l2[i]
#     return d

# print(merge_list(["a", "b", "c"], [1, 2, 3]))

# # 3


# def contactsCRUD():
#     contacts = {"Nodir": "+998918602711", "Laziz": "+998908002534"}
#
#     while True:
#         print("Quyidagi buyruqlardan birini tanlang!")
#
#         print("""
#         1 - kontakt qo'shish
#         2 - kontakt yangilash
#         3 - kontakt o'chirish
#         4 - kontakt qidirish
#         5 - kontaklarni ko'rish
#         0 - dasturdan chiqish
#         """)
#         try:
#             user_button = input("buyruq: ")
#             if (user_button == '1' or user_button == '2'
#                 or user_button == '3' or user_button == '4' or user_button == '5' or user_button == '0'):
#                 pass
#             else:
#                 print("❗Bunday buyruq yo'q\n")
#                 continue
#         except:
#             print("❗Bunday buyruq yo'q\n")
#             continue
#
#         if user_button == '1':
#             name = input("Ism kiriting: ").title()
#             number = input("Nomerni kiriting: ")
#             contacts[name] = number
#             print("Kontakt muvaffaqiyatli qo'shildi!\n")
#
#         elif user_button == '2':
#             name = input("Ism kiriting: ").title()
#             number = input("Nomerni kiriting: ")
#             contacts[name] = number
#             print("Kontakt muvaffaqiyatli yangilandi!\n")
#
#         elif user_button == '3':
#             name = input("Ism kiriting: ").title()
#             if contacts.get(name):
#                 del contacts[name]
#                 print("Kontakt muvaffaqiyatli o'chirildi!\n")
#             else:
#                 print("bunday kontakt yo'q\n")
#                 continue
#
#         elif user_button == '4':
#             name = input("Ism kiriting: ").title()
#             if contacts.get(name):
#                 print(name, contacts[name])
#             else:
#                 print("❌ bunday kontakt yo'q\n")
#
#         elif user_button == '5':
#             print(contacts)
#
#         elif user_button == '0':
#             print("Dasturdan chiqdingiz!")
#             break
#
#         else:
#             continue
#
# contacts_CRUD()

# # 4
# def counter_dict(nums):
#     """sonlar listni qabul qilib ichida nechta son necha marta takrorlanganini sanab qaytaruvchi funksiya"""
#     return dict(Counter(nums))


# print(counter_dict([2, 1, 1, 1]))

# # 5
# def max_ball_students(talabalar):
#     """talabalar dict ni qabul qilib max ball olgan 2 ta talabalarni dict ko'rinishida qaytaruvchi funksiya"""
#     new_talabalar = deepcopy(talabalar)
#     d = {}
#
#     mx_stu_1 = max(new_talabalar, key=new_talabalar.get)
#     d[mx_stu_1] = new_talabalar[mx_stu_1]
#
#     del new_talabalar[mx_stu_1]

# mx_stu_2 = max(new_talabalar, key=new_talabalar.get)
# d[mx_stu_2] = new_talabalar[mx_stu_2]
#
# return d

# print(max_ball_students({"Akmal": 64, "Doston": 84, "Tohir": 55, "Nodir": 76, "Zafar": 68}))
# -=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=--==-=-=-=-=-=-=-=-=--=-=-=-=-=-=

# car1 = {
#     'brand': 'bmw',
#     'model': 'bmw x6',
#     'year': 2023
# }
# car2 = {
#     'brand': 'mersedes',
#     'model': 'c 220',
#     'year': 2022
# }
# car1.update(car2)
# print(car1)

# soz = 'TeLefOn'
#
# lower_letters = ''
# for i in soz:
#     if i.islower():
#         lower_letters += i
# print(lower_letters)


# a = 'olma'
# b = 'anor'
# c = ''
# for i in range(len(a)):
#     c += a[i] + b[i]
# print(c)
