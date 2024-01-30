# #def sanoq():
#     for i in range(1,41):
#         if i%2==0 and i%3==0:
#             print(i)

# sanoq()
# #-------------------------------------------------------------------------------------------------------------
# # 1
# def user_data(first_name, last_name, age):
#     print(f"Ism: {first_name}\
#             \nFamiliya: {last_name}\
#             \nYosh: {age}")

# f_name = input('Ism: ')
# l_name = input('Familya: ')
# age = input('Yosh: ')
# user_data(f_name,l_name,age)

# # 2
# def find_max(a,b,c):
#     if a>b and a>c:
#         print(a)
#     elif b>c:
#         print(b)
#     else:
#         print(c)

# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))

# find_max(a,b,c)

# # 3
# def find_letter_count(word,letter):
#     print(word.count(letter))

# word = input("So'z kiriting: ")
# letter = input("Harf kiriting: ")

# find_letter_count(word,letter)

# # 4
# def list_num(mylist):
#     print(sum(mylist))

# list_1 = [32,5,6,4,45]
# list_num(list_1)

# # 5
# def daraja(a,b):
#     return a**b

# print(daraja(2,3))

# # 6
# def daraja4(a,b,c,d):
#     print(a**b)
#     print(c**d)

# daraja4(2,3,3,2)

# # 7
# def digit_count_and_sum(word):
#     count_num = 0
#     yigindi = 0
#     for letter in word:
#         if letter.isdigit():
#             count_num+=1
#             yigindi+=int(letter)
#     print(f"Sonlar yig'indisi: {yigindi} ta\nSonlar {count_num} ta qatnashgan")

# word_input = input("So'z: ")
# digit_count_and_sum(word_input)

# # 8
# def add_right(a, b):
#     print(f"{a}{b}")

# add_right(344,3245)

# # 9
# def add_left(a, b):
#     print(f"{b}{a}")

# add_left(44,32)

# # 10
# def work_with_list(a):
#     min_num = min(a)
#     for i in range(len(a)):
#         a[i] **= min_num
#     return a

# print(work_with_list([2, 3, 4, 5, 6, 7, 8, 9]))

# # 11
# def big_sales(sales):
#     month = list(sales.keys())[0]
#     salary = list(sales.values())[0]
#     for key,values in sales.items():
#         if salary<values:
#             month=key
#             salary=values
#     return month

# def big_sales(sales):
#     return max(sales,key=sales.get)

# print(big_sales({
#     "yanvar": 12000,
#     "mart": 6000,
#     "aprel": 15000,
#     "sentabr": 9000,
#     "dekabr": 10000,
# }))

# # 12
# def min_max(numbers, max_num, min_num):
#     if max(numbers)==max_num:
#         print(max_num,"numbers ichidagi eng katta son")
#     else:
#         print(max_num,"numbers ichidagi eng katta son emas")
#     if min(numbers)==min_num:
#         print(min_num,"numbers ichidagi eng kichik son")
#     else:
#         print(min_num,"numbers ichidagi eng kichik son emas")

# min_max([3,5,12,63,41,39,86,4],85,4)

# # 13
# def expensiveProduct(products):
#     p_name = products[0]['name']
#     p_price = products[0]['price']
#     for p in products:
#         if p_price<p['price']:
#             p_name=p['name']
#             p_price=p['price']
#     return p_name

# def expensiveProduct(products):
#     return max(products)

# mylist = [
#   {
#     "name": "Iphone X",
#     "price": 600
#   },
#   {
#     "name": "Iphone 12",
#     "price": 1500
#   },
#   {
#     "name": "Samsung Note 9",
#     "price": 800
#   },
#   {
#     "name": "Samsung S10",
#     "price": 1100
#   },
# ]
# print(expensiveProduct(mylist))

# # -=-=-=-=-=-=-=-=-=-=-=-=-=-=qayta yechim-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# # 1
# def user_data(first_name, last_name, age):
#     print(f"""
#  * * * * * * * * * * * * * * *
#  *      Ism: {first_name}       *
#  * * * * * * * * * * * * * * *
#  *    Familiya: {last_name}    *
#  * * * * * * * * * * * * * * *
#  *         Yosh: {age}          *
#  * * * * * * * * * * * * * * *""")


# user_data("Sardorbek", "Makhmudov", 21)

# # 3
# def min_max(numbers, max_num, min_num):
#     print(f"Max: {max(numbers) == max_num}\nMin: {min(numbers) == min_num}")
#
#
# min_max([8, 5, 6, 7, 4, 3], 8, 3)

# # 11
# my_dict = {
#     "yanvar": 12000,
#     "mart": 6000,
#     "aprel": 15000,
#     "sentabr": 9000,
#     "dekabr": 10000,
# }

# def big_sales1(sales):
#     bg_sal = max(sales.values())
#     for k in sales.keys():
#         if sales[k] == bg_sal:
#             return k
# # 11 2-usul
# def big_sales2(sales):
#     return max(sales, key=sales.get)

# print(big_sales1(my_dict))
# print(big_sales2(my_dict),1)

# # 12
# def expensiveProduct(products):
#     max_phone = list(products[0].values())[0]
#     max_price = list(products[0].values())[1]
#     for i in products:
#         if list(i.values())[1] > max_price:
#             max_phone = list(i.values())[0]
#             max_price = list(i.values())[1]
#     return max_phone


# print(expensiveProduct([
#     {
#         "name": "Iphone X",
#         "price": 600
#     },
#     {
#         "name": "Iphone 12",
#         "price": 1500
#     },
#     {
#         "name": "Samsung Note 9",
#         "price": 800
#     },
#     {
#         "name": "Samsung S10",
#         "price": 1500
#     },
# ]))

# ism=input('ismingiz ')
# print(f'''
# ***********
# * {ism} *
# ***********''')

# #-=-=--=-===-=-=-=-=-=-=-=-=-=-=-==F-18. 8-dars-=-=-=--=-=-=-=--=-=-=-------=-=-=-=-=--=-=-=-=-=-=-=
# #-=-=--=-===-=-=-=-=-=-=-=-=-=-=-===-=-=-=-==-=-=-=-=--=-=-=-=--=-=-=-------=-=-=-=-=--=-=-=-=-=-=-=

# """
# ******
# ******
# ******
#
# *  *  *  *  *  *
# *              *
# *              *
# *              *
# *              *
# *  *  *  *  *  *
#
# *
# ***
# *****
# *******
# *********
# """

# # 1
# for j in range(4):
#     if j == 1 or j == 2:
#         print("*", "\t", "*")
#     else:
#         print("*" * 6)
# print()

# for a in range(1, 7):
#     if a == 1 or a == 6:
#         print("*  " * 6)
#     else:
#         print("*", "\t\t\t  ", "*")

# print()
# # 2
# for i in range(1, 10, 2):
#     print("*" * i)

# #-=-=--=-===-=-=-=-=-=-=-=-=-=-=-===-Vazifalar=-=-=-==-=-=-=-=--=-=-=-=--=-=-=-------=-=-=-=-=--=-=-=-=-=-=-=
# def sortList(my_list, kamayish):
#     if kamayish == False:
#         if len(my_list) <= 1:
#             return my_list
#         else:
#             piwod = my_list[0]
#             left_list = [i for i in my_list[1:] if i <= piwod]
#             right_list = [i for i in my_list[1:] if i > piwod]
#             return sortList(left_list, False) + [piwod] + sortList(right_list, False)
#     if kamayish == True:
#         if len(my_list) <= 1:
#             return my_list
#         else:
#             piwod = my_list[0]
#             right_list = [i for i in my_list[1:] if i > piwod]
#             left_list = [i for i in my_list[1:] if i <= piwod]
#             return sortList(right_list, True) + [piwod] + sortList(left_list, True)
#
#
# print(sortList([5, 7, 2, 2, 73, 6, 17, 8], False))
# print(sortList([5, 7, 2, 2, 73, 6, 17, 8], True))

# -=-=-=-=-=-=-=-=-=-= 7 ta misol-=-=-=-==-=-=-=-=-==-=-=-
# # 1 sort metodidan foydalanmasdan listni sortlash kamayish yoki ko'payish tartibida
def sortList(my_list, kamayish):
    if kamayish == True:
        for i in range(len(my_list)):
            for j in range(i + 1, len(my_list)):
                if my_list[i] >= my_list[j]:
                    my_list[i], my_list[j] = my_list[j], my_list[i]
    elif kamayish == False:
        for i in range(len(my_list)):
            for j in range(i + 1, len(my_list)):
                if my_list[i] <= my_list[j]:
                    my_list[i], my_list[j] = my_list[j], my_list[i]
    return my_list


# print(sortList([5, 7, 2, 2, 73, 6, 17, 8], False))
# print(sortList([5, 7, 2, 2, 73, 6, 17, 8], True))

# #2 Uch ta funksiya yordamida min max ni topib max ni min darajasini topish
def find_max(my_list):
    mx_num = 0
    for i in my_list:
        if mx_num < i:
            mx_num = i
    return mx_num


def find_min(my_list):
    mn_num = sorted(my_list)[0]
    return mn_num


numbers = [5, 4, 2, 3, 6, 7, 10, 6]


# def power_max_min():
#     maxElem = find_max(numbers)
#     minElem = find_min(numbers)
#     return maxElem ** minElem


# print(power_max_min())

# #3
def find_last_region(regions):
    last = regions[0][1]
    for region in regions:
        if region[1] not in [i[0] for i in regions]:
            last = region[1]
            break
    return last


# result = find_last_region(
#     [['Toshkent', 'Buxoro'], ['Buxoro', 'Samarqand'], ["Andijon", "Farg'ona"], ["Samarqand", "Andijon"]])
# print(result)


# # 4 toq sonlarni yangi listga solib qaytarish
def findOdd(my_list):
    return list(filter(lambda x: x % 2 != 0, my_list))


# print(findOdd([9, 6, 3, 7, 3, 22, 64, 13, 54, 879, 4, 21, 1, 78]))

# #5 juft sonlarni yangi listga solib qaytarish
def findEven(my_list):
    return list(filter(lambda x: x % 2 == 0, my_list))


# print(findEven([9, 6, 3, 7, 3, 22, 64, 13, 54, 879, 4, 21, 1, 78]))

# # 6
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 5]


def odd_vs_even(oddlist, evenlist):
    sum_odd = sum(oddlist(numbers2))
    sum_even = sum(evenlist(numbers2))
    print(sum_odd, sum_even)
    return "oddlist" if sum_odd > sum_even else "evenlist"


# print(odd_vs_even(findOdd, findEven))


# def find_last_region(regions):
#     new_list = []
#     for i in range(len(regions)):
#         print(i)
#         if regions[i][i + 1] == regions[i + 1][i]:
#             new_list.append(regions[i])
#
#     return new_list


# # 7
phones = [{'brand': 'Samsung', 'model': 'A51', 'size': 128, 'color': 'Grey'}]


def add_phones(brand, model, size, color):
    phones.append(
        {"brand": brand,
         'model': model,
         'size': size,
         'color': color}
    )
    return phones


def get_phones():
    for i in phones:
        print(f"""
        ------------------------------------------------------
        |    {list(i.keys())[0]}     |{str(list(i.values())[0]).center(37)}|
        ------------------------------------------------------
        |    {list(i.keys())[1]}     |{str(list(i.values())[1]).center(37)}|
        ------------------------------------------------------
        |    {list(i.keys())[2]}      |{str(list(i.values())[2]).center(37)}|
        ------------------------------------------------------
        |    {list(i.keys())[3]}     |{str(list(i.values())[3]).center(37)}|
        ------------------------------------------------------""", end="")


def play():
    while True:
        user_comand = input("\n'add', 'list' yoki 'exit' komandalaridan birini kiriting: ")

        if user_comand == "add":
            user_dates = []
            examples = ['brand', 'model', 'size', 'color']
            for i in range(4):
                user_dates.append(input(f"{examples[i]}: ").title())
            add_phones(user_dates[0], user_dates[1], user_dates[2], user_dates[3])
            user_dates.clear()

        if user_comand == "list":
            get_phones()

        if user_comand == 'exit':
            break


# play()
