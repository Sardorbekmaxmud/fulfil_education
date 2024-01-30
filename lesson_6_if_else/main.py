# # 1
# son = int(input("son kiriting: "))
# if son>=0:
#     print('musbat')
# else:
#     print("manfiy")
import math

# # 2
# son = int(input("son kiriting: "))
#
# if son%2==0:
#     print("juft")
# else:
#     print("toq")

# # 3
# week = ["Dushanba","Seshanba","Chorshanba","Payshanba","Juma","Shanba","Yakshanba"]
#
# son = int(input("son kiriting: "))
# if son>0 and son<=7:
#     print(week[son - 1])
# else:
#     print("bunday hafta kuni yo'q")

# # 4
# a = int(input("son kiriting: "))
#
# if a>=0:
#     print(a+2)
# else:
#     print(a-2)

# # 5
# a = int(input("a:  "))
# b = int(input("b:  "))
#
# if a>3 and b<=6:
#     print("rost")
# else:
#     print("xato")

# # 6
# a = int(input("a:  "))
# b = int(input("b:  "))
#
# if a<2 and b>=-2:
#     print("rost")
# else:
#     print("xato")

# # 7
# a = int(input("a:  "))
# b = int(input("b:  "))
#
# if a>b:
#     print(f"a:{a},b: {b}")
# else:
#     print(f"b:{b},a:{a}")

# # 8
# a = float(input("a: "))
# b = float(input("b: "))
#
# if int(str(a).split(".")[1]) < int(str(b).split(".")[1]):
#     print(a, "sonini qoldig'i kichik")
# elif int(str(a).split(".")[1]) == int(str(b).split(".")[1]):
#     print(f"{a} = {b}")
# else:
#     print(b, "sonini qoldig'i kichik")

# # 9
# a = int(input("a:  "))
# b = int(input("b:  "))
# c = int(input("c:  "))
#
# if a<b<c:
#     print('rost')
# else:
#     print("xato")

# # 10
# a = int(input("a:  "))
# b = int(input("b:  "))
# c = int(input("c:  "))
# #
# if b>a and b<c or b<a and b>c:
#     print("b o'rtada, rost")
# elif b<a and b<c:
#     print("b boshida, xato")
# elif a==b==c:
#     print("teng")
# else:
#     print("b oxirida, xato")

# # 11
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
#
# count = 0
# if a>0:
#     count+=1
# if b>0:
#     count+=1
# if c>0:
#     count+=1
# print(count)

# # 12
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
#
# hisob = 0
# if a>b and a>c:
#     if b>c:
#         hisob+=a+b
#     else:
#         hisob+=a+c
# elif b>c:
#     if a>c:
#         hisob+=b+a
#     else:
#         hisob+=b+c
# else:
#     if a>b:
#         hisob+=c+a
#     else:
#         hisob+=c+b
# print(hisob)

# # 13.1 men ishlagan usul
# a = int(input("a: "))
#
# tub = True
# if a<=1:
#     tub = False
# elif a==2:
#     tub=True
# else:
#     for i in range(2,a):
#         if a%i==0:
#             tub=False
#
# if tub:
#     print(f"{a} tub son")
# else:
#     print(f"{a} tub son emas")

# # 13.2 Komiljon aka ishlagan usul
# import math
#
# a = int(input("Son kiriting:\n"))
# chegara = int(math.sqrt(a))
#
# for i in range(2,chegara+1):
#     if a % i == 0:
#         print("tub son emas")
#         break
# else:
#     print("tub son")

# # 14
# a = int(input("a:  "))
# b = int(input("b:  "))
#
# if a%2!=0 and b%2!=0:
#     print("rost,toq sonlar")
# else:
#     print('xato')

# # 15
# a = int(input("a:  "))
# b = int(input("b:  "))
#
# if a%2!=0 or b%2!=0:
#     print("rost,toq sonlar")
# else:
#     print('xato')

# # 16
# a = int(input("a:  "))
# b = int(input("b:  "))
# c = int(input("c:  "))
#
# if a>0 and b>0 and c>0:
#     print(True)
# else:
#     print(False)

# # 17
# a = int(input("a: "))
#
# if a%2==0 and a>9 and a<100:
#     print(True)
# else:
#     print(False)

# # 18
# a = int(input("a: "))
#
# if a%2!=0 and a>99 and a<1000:
#     print(True)
# else:
#     print(False)

# # 19
# son = input("son kiriting: ")
# if son[0]==son[1]==son[2]:
#     print("xato")
# else:
#     print("rost")

# # 20
# son = int(input("son kiriting: "))
# if son>0:
#     print(f"musbat, {len(str(son))}")
# else:
#     print(f"manfiy, {len(str(son))-1}")

# # 21
# son = input("son kiriting: ")
# if int(son[0])<int(son[1])<int(son[2]) and len(son)==3:
#     print("o'sich tartibida")
# elif int(son[0])>int(son[1])>int(son[2]) and len(son)==3:
#     print("kamayish tartibida")
# else:
#     print("xato")

# # 22 ❓✅ to'rt xonali sonni chap va o'ngga to'g'ri o'qilishini tekshirish
# four_room_num = int(input("son: "))
# if str(four_room_num)[::-1][2:] == str(four_room_num)[2:]:
#     print("To'g'ri")
# else:
#     print("Noto'g'ri")


# # 23
# x = int(input("x: "))
# y = int(input("y: "))

# if x>0 and y>0:
#     print("I chorak")
# elif x<0 and y>0:
#     print("II chorak")
# elif x<0 and y<0:
#     print("III chorak")
# else:
#     print("IV chorak")

# # 24 ❓


# # 25 ❓


# # 26
# x1 = int(input("x1: "))
# y1 = int(input("y1: "))
# x2 = int(input("x2: "))
# y2 = int(input("y2: "))

# if abs(x1-x2)==abs(y1-y2) or abs(x1-x2)==1 and abs(y1-y2)==0 or abs(x1-x2)==0 and abs(y1-y2)==1:
#     print("mumkin")
# else:
#     print('mumkin emas')

# # 27
# x1 = int(input("x1: "))
# y1 = int(input("y1: "))
# x2 = int(input("x2: "))
# y2 = int(input("y2: "))

# if abs(x1-x2)==abs(y1-y2):
#     print("mumkin")
# else:
#     print('mumkin emas')

# # 28 ❓✅

# # 29
# n = int(input("(1-7) oralig'ida son kiriting: "))
# k = int(input("(1-365) oralig'ida son kiriting: "))
#
# weeks = ["Dushanba","Seshanba","Chorshanba","Payshanba","Juma","Shanba","Yakshanba"]

# """
# n = 6

# k = 34
# j = 4

# n = 2                       --> 1 -yanvar

# k = 7
# j = 1

# n = 3 k%7+(n-1)

# k = 18
# j = 6


# """
# print((k % 7 + (n - 1))-1)
# print(weeks[(k % 7 + (n - 1))-1])

# print(n-(k%7),k%7)
# print(weeks[((k%7)+(n-1))-1])
# print(weeks[((k-(7-n))%7)-2])


# ----------------------qayta yechimlar---------------------------------------
# 23
# x = int(input('x: '))
# y = int(input('y: '))
#
# if x > 0 and y > 0:
#     print('I chorak')
# elif x < 0 and y > 0:
#     print('II chorak')
# elif x < 0 and y < 0:
#     print('III chorak')
# elif x > 0 and y < 0:
#     print('IV chorak')
# else:
#     print("O o'qi")

# ----------shaxmat taxtasi---------------
# 26 shoxni yurishi ️️️️♟️
# x1 = int(input('x1: '))
# y1 = int(input('y1: '))
# x2 = int(input('x2: '))
# y2 = int(input('y2: '))
#
# if (abs(x1 - x2) == abs(y1 - y2)) or (x1 == x2 and abs(y1 - y2) == 1) or (y1 == y2 and abs(x1 - x2) == 1):
#     print('Yura oladi')
# else:
#     print('Yura olmaydi')

# 27 filni yurishi ️️️️️️♟️️️️️
# x1 = int(input('x1: '))
# y1 = int(input('y1: '))
# x2 = int(input('x2: '))
# y2 = int(input('y2: '))

# if abs(x1 - x2) == abs(y1 - y2):
#     print('yura oladi')
# else:
#     print('yura olmaydi')

# 28 farzinni yurishi ♟️
# x1 = int(input('x1: '))
# y1 = int(input('y1: '))
# x2 = int(input('x2: '))
# y2 = int(input('y2: '))
#
# if (abs(x1 - x2) == abs(y1 - y2)) or (x1 == x2 and y1 < y2 or y1 > y2) or (y1 == y2 and x1 < x2 or x1 > x2):
#     print('yura oladi')
# else:
#     print('yura olmaydi')
