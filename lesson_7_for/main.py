# name = input("Ismingizni kiriting:\n")
# interes = input("Qiziqishlaringizni kiriting:\n")

# # if any([x in interes for x in ['kitob','kutubxona']]):
# if 'kitob' in interes or "kutubxona" in interes:
#     book_lib = input('qanday kitoblar yoqadi?\n')
#     if "detektiv" in book_lib:
#         book = input("shaytanat kitobi haqidagi fikringiz?\n")
#         print("Raxmat, fikrlaringiz uchun!")
#     elif "diniy" in book_lib:
#         print("Sizga 'Hadis va hayot' kitoblar to'plamini sovg'a qilamiz!")
#     else:
#         print("Ajoyib narsalarga qiziqar ekansiz!")
# elif 'sport' in interes:
#     savol = input("qaysi sport turiga qiziqasiz?\n")
#     if 'futbol' in savol:
#         f_club = input("qaysi komandani yoqtirasiz?\n")
#         if "real" in f_club or 'barsa' in f_club:
#             print("el-classicoga chipta sovg'a qilamiz!🎉")
#         else:
#             print("Ajoyib, komandangizga zafarlar tilaymiz")
#     else:
#         print("Sport bilan shug'ullanish sog'lik garovi")
# else:
#     print("Ko'p narsalarga qiziqar ekansiz, bu ajoyib!")


# --------------------------Homework--------------------------------------------------

# # 1
# k = int(input("k: "))
# n = int(input("n: "))

# for i in range(n):
#     print(k)

# # 2
# n = int(input("n: "))
# answer = 0
# for i in range(1,n+1,2):
#     answer+=i
# print(answer)

# # 3
# n = int(input("n: "))
# answer = 0
# for i in range(n+1):
#     if i%3==0 and i%9!=0:
#         answer+=i
# print(answer)

# # 4
# n = int(input("n: "))
# answer = 0
# for i in range(1,n+1):
#     answer+=i**2
# print(answer)

# # 5
# word = list(input('so\'z kiriting '))
#
# for i in range(len(word)):
#     n = int(input(f"1-{len(word)} oralig'ida son kiriting "))
#     word.pop(n-1)
#     print(''.join(word))

# # 6
# price = int(input("narxni kiriting: "))
# if price>100_000:
#     print(f"sizga {(price*90)//100} so'm")
# elif price > 50_000:
#     print(f"sizga {(price*95)//100} so'm")
# else:
#     print(f"{price} so'm")

# # 7
# natija=[]
# a = int(input("a: "))
# b = int(input("b: "))
# for i in range(b-1,a,-1):
#     natija.append(i)
#     print(i)
# print("Uzunligi: ",len(natija))


# # 8
# sweet_price = int(input("kanfet narxi: "))
# for kg in range(1,11):
#     print("{} kg narxi: {:,} so'm".format(kg,kg*sweet_price))

# # 9
# sweet_price = int(input("kanfet narxi: "))
# for kg in range(1,11):
#     print("{} kg narxi: {:,} so'm".format(kg/10,kg/10*sweet_price))

# # 10
# natija=0
# a = int(input("a: "))
# b = int(input("b: "))
# for i in range(a,b+1):
#     natija+=i**2
#     print(f"{i} kvadrati = {i**2}")
# print("yig'indi: ",natija)

# # 11
# a = int(input("a: "))
# n = int(input("n: "))
# for i in range(1,n+1):
#     print(f"{a} ning {i} darajasi = ",a**i)

# # 12 factorial
# son = int(input("son kiriting: "))
# natija = 1
# for i in range(1,son+1):
#     natija*=i
# print(natija)


# ---------------qayta yechim----------------------------
# mustaxkamlash uchun misol
# from colorama import Fore
#
# user_name = input('Ismingiz: ')
# user_interested = input("Qiziqishlaringiz: ")
#
# if 'kitob' in user_interested or 'kutubxona' in user_interested:
#     user_inter_books = input("Qanday kitoblarni yoqtirasiz?\n")
#
#     if 'detektiv' in user_inter_books:
#         answer = input("Shaytanat kitobi haqida fikringiz?\n")
#         print("Ajoyib, sizning fikrlaringiz juda qiziqarli!")
#     elif 'diniy' in user_inter_books:
#         print(f"{Fore.LIGHTWHITE_EX}Sizga {Fore.BLUE+'Hadis va hayot'} {Fore.LIGHTWHITE_EX}kitobini sovg'a qilamiz!")
#     else:
#         print(f"{user_name}, qiziqishlaringiz juda ajoyib ekan!")
#
# elif 'sport' in user_interested:
#     user_inter_sport = input("Qaysi sport turlariga qiziqasiz?\n")
#
#     if 'futbol' in user_inter_sport:
#         user_inter_groups = input("Qaysi komandani yoqtirasiz?\n")
#
#         if 'real' in user_inter_sport or 'barsa' in user_inter_sport:
#             print("Siz El-classicoga chipta sovg'a qilamiz!")
#         else:
#             print(f"{user_name}, komandangiz zo'r o'ynasa kerak-a?")
#     else:
#         print(f"{user_name}, sport sog'lik garovi! Sport bilan doimiy shug'ullaning!")
# else:
#     print("Siz ajoyib narsalarga qiziqar ekansiz!")


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=saytdagi qo'shimcha misollar-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=
##2
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()

# # 18
# n = 6
# for i in range(1, n):
#     for j in range(1, i + 1):
#         print("*", end=" ")
#     print()
# for k in range(n-2,0,-1):
#     for l in range(k):
#         print("*", end=" ")
#     print()

# # 4
# numbers = [12, 75, 150, 180, 145, 525, 50]
#
# for i in numbers:
#     if i > 500:
#         break
#     if i > 150:
#         continue
#     if i % 5 == 0:
#         print(i)

# # 11
# import math
# start = 25
# end = 50
#
# for i in range(start,end):
#     for j in range(2,int(math.sqrt(i))+1):
#         if i % j == 0:
#             break
#     else:
#         print(i)

# # 12 --------fibonacci-----------
# a = 0
# b = 1
#
# fib_numbers = [0,1]
# for i in range(8):
#     a = a + b
#     b = fib_numbers[-1]
#     fib_numbers.append(a)
# print(fib_numbers)

# # 17
# n = 5
# str_num = 0
#
# for i in range(1,n+1):
#     str_num+=int("2"*i)
#
# print(str_num)

# =-=-======-=-==-=--=-==--=-=-=-=-====-

# array = list(range(20))
#
# uzunlik = len(array)
#
# while uzunlik > 0:
#     if array[uzunlik - 1] % 2 == 0:
#         uzunlik -= 1
#         continue
#     print(array[uzunlik - 1], end=' ')
#     uzunlik -= 1
