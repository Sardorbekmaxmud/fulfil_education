# # 1
# listni ichidagi sonlarni toqlarini ajratib olish

# l = list(range(1,6))

# toqlar = {i*2 for i in l if i%2==1}
# print(toqlar)

# # 2==================================================================================
## regions = [["Toshkent", "Buxoro"], ["Farg'ona", "Jizzax"], ["Jizzax", "Navoiy"], ["Andijon", "Farg'ona"],
#            ["Samarqand", "Andijon"], ["Buxoro", "Samarqand"]]

# from_city = [l[0] for l in regions]
# to_city = [l[1] for l in regions]
# print(from_city)
# print(to_city)

# # 3==========================================================================
# lst = ['Alice', 1, 2, 3, 'Alice', 'Alice']
# index_all = [i for i in range(len(lst)) if lst[i]=='Alice']
# print(index_all)

# # 4==============================================================================
# people = [("John", 240_000), ("Alice", 120_000), ("Ann", 1_100_000), ("Zach", 44_000), ("Doe", 2_300_000)]
# mil_search = [name for name,money in p if money>=1_000_000]
# print(mil_search)

# def milloner_find(p):
#     mil_search = [name for name,money in p.items() if money>=1_000_000]
#     return mil_search
#
# # for test millioner func
# people_data1 = {'Alice': 1_000_000, 'Bob': 998_170, 'Carol': 1_229_080, 'Frank': 881_230, 'Eve': 93_121}
# people_data2 = {'Alice': 1_000_000, 'Bob': 998_170, 'Frank': 1_881_230, 'Eve': 93_121}
#
# def test():
#     assert milloner_find(people_data1)==['Alice','Carol']
#     assert milloner_find(people_data2)==['Alice','Frank']
#
# test()


# # 5==========================================================================
# answer = [(i,j) for i in range(3) for j in range(3)]
# print(answer)

# # 6==========================================================================================
# text = '''Call me Ishmael. Some years ago - never mind how long precisely - having little
# or no money in my purse, and nothing particular to interest me on shore, I thought I would
# sail about a little and see the watery part of the world. It is a way I have of driving off
# the spleen, and regulating the circulation. - Moby Dick '''

# size_fifth_and_more = [i for i in text.split() if len(i)>=5 and i.isalnum()]
# print(size_fifth_and_more)

# # 6 version = 2
# line_size_and_more = [[i for i in line.split() if len(i)>7 and i.isalnum()] for line in text.split('\n')]
# print(line_size_and_more)

# # 6 ning 2-misol ziplash====================================================================
# key = ('name','lname','age')
# value = ('rustam','umarov',25)
#
# test = [i for i in zip(key,value)]
# print(test)

# # unziplash
# key_new, value_new = zip(*test)
# print(list(key_new))
# print(list(value_new))


# # 7 ============================================================================================
# car = ['brand','model','year','price']

# car_list_to_value = [('BMW','M5','2009',35000),
#                      ('Ford','Fucs','2021',43000),
#                      ('Audi','A8','2018',67000),
#                      ('Mers','A208','2022',125000),
#                      ('Nissan','GTR','2013',24500),]

# all_db = [dict(zip(car,line)) for line in car_list_to_value]
# print(all_db)

##===================lamba learn========================
# f = lambda x: x*2
# print(f(3))
# # 8=======================LAMBDA FUNC==========================================================================
# add_three_num = lambda a,b,c: a+b+c
# print(add_three_num(4,5,6))

# print((lambda a,b,c: a+b+c)(1,2,3))

# print((lambda a: a+3)(9))

# # 9 =======================map()==================================
## lsitdagi str larni int qilib beradi
# str_list = ['1','2','3','4','5','6','7','2']

# str_to_int = list(map(int,str_list))
# print(str_to_int)

# # 10============================================================
## listdagi sonlarni darajaga ko'paytirib listga soladi
# list_num = [2,3,5,6,9]

# print(list(map(lambda x: x**2,list_num)))

# # 11============listdagi elementlarni mos indexi bo'yicha ayiring.==================================================
# print(list(map(lambda x,y: x-y,[2,4,6],[1,3,5])))

# # 12==================================listdagi str larni upper qilish========================
# str_list = ['matn','string','katta son']
# print(list(map(str.upper, str_list)))

# # 13
# from functools import reduce

# print(reduce(lambda x,y: x*y,range(1,4)))

# # 14 filter==============loop da y ayalanib true qaytarsa qabul qiladi
# nums = [12,6,3,34,2,5,7]
# results = list(filter(lambda x: x%2==0,nums))
# print(results)


# print('hi','my','friends',sep='-')


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-
# ticet = [["Toshkent", "Buxoro"], ["Farg'ona", "Jizzax"], ["Jizzax", "Navoiy"], ["Andijon", "Farg'ona"],
#          ["Samarqand", "Andijon"], ["Buxoro", "Samarqand"]]
#
# from_city = [i[0] for i in ticet]
# print(from_city)

# l = [1, 2, 3, 'alise', 'alise']
#
# index_ = [i for i in range(len(l)) if l[i] == 'alise']
# print(index_)

# people = [('John', 240_000), ("Alice", 120_000), ("Anna", 1_100_000), ('Zach', 44_000)]
# millioners = (name for name, money in people if money >= 1_000_000)
#
# gen = [i for i in millioners]
# print(gen)


# def find_millioners(people):
#     return [name for name, money in people.items() if money >= 1_000_000]


# people_millioner1 = {"Akmal": 123_000, "Furqat": 450_000_000, "Gulshoda": 534_000}
# people_millioner2 = {"Po'lat": 451_000, "Elbek": 50_000_000, "Gulshoda": 999_542, "Botir": 322_222_222}


# def test_millioners():
#     assert find_millioners(people_millioner1) == ["Furqat"]
#     assert find_millioners(people_millioner2) == ["Elbek", "Botir"]


# test_millioners()

# t = [(i, j) for i in range(3) for j in range(3)]
# print(t)

# text = '''Call me Ishmael. Some years ago - never mind how long precisely - having little
# or no money in my purse, and nothing particular to interest me on shore, I thought I would
# sail about a little and see the watery part of the world. It is a way I have of driving off
# the spleen, and regulating the circulation. - Moby Dick '''

# len_five_word_rule = [i for i in text.split() if len(i) == 5]
# len_five_word_space = [[j for j in i.split() if len(j) > 7] for i in text.split('\n')]
# print(len_five_word_rule) # hammasini birdan ajratish
# print(len_five_word_space) # qatorma qator olib ajratish

# # -=-=-===-=-=-=ziplash=-=-=-=-=-=---==-=-==-=-=-
# key = ['model', 'color', 'year', 'price']
# value = ['BMW', 'Grey', 2023, 185_000]
#
# car_1 = [i for i in zip(key, value)]
# print(car_1)
#
# -=-=-=-=-=-=-=-unziplash-=-=-=-=-=-=-=-=-=-=-
# keys, values = zip(*car_1)
# print(keys)
# print(values)

# -==-==-==7
# ustun_nomlari = ['name', 'salary', 'job']
# qatorlar = [('Alice', 180_000, 'data scientist'),
#             ('Bob', 99_000, 'project manager'),
#             ('Frank', 87_000, 'backend developer')]
#
# db = [dict(zip(ustun_nomlari,i)) for i in qatorlar]
# print(db)

# print((lambda a, b, c: a + b + c)(1, 2, 3))

# numbers = list(map(lambda n: int(n), ["1", "2", "3", "4", "5"]))
# print(numbers)


# #=-=-=-=-=-=------------------F-18-guruh 9-dars--------=================-------------==========---------=====
# def bubble_sort(lst):
#     for i in range(len(lst)):
#         for j in range(i + 1, len(lst)):
#             if lst[i] > lst[j]:
#                 lst[i], lst[j] = lst[j], lst[i]
#
#     return lst

# # short form
# def bubble_sort(lst):
#     [lst.append(lst.pop(0) if j == len(lst) - 1 or lst[0] < lst[1] else lst.pop(1)) for i in range(len(lst)) for j in range(len(lst))]
#     return lst
#
#
# print(bubble_sort([8, 4, 8, 5, 4, 2, 6, 7, 5, 0, -4, 9, -3]))

# quick_sort = lambda x: x and quick_sort([i for i in x[1:] if i <= x[0]]) + [x[0]] + quick_sort([i for i in x[1:] if i > x[0]])
#
# print(quick_sort([5, 4, 2, 6, 7, 15, 0, -4, 9, -3]))


# ---------------------homework vazifa.txt file -=-=-=-=====-=-=-=-=-=-=--=-=-=-==-=-=-=-==-=-=-=-=-=-=-=-=
# #Oson-1. longWord(word1, word2) - bu funksiya berilgan ikkita string eng uzunini print qilib bersin.
# def longWord(word1, word2):
#     return word1 if len(word1) > len(word2) else word2 if len(word1) < len(word2) else "teng"
#
#
# print(longWord("123456", "1234655"))

# #Oson-2. wordCount(matn) - bu funksiya berilgan matndan nechta so'z borligini aniqlab sonni return qiladi.
# Masalan: "Python Django Hello Apple Network" da 5 ta so'z bor.

# def wordCount(matn):
#     return len(matn.split())
#
#
# print(wordCount("Python Django Hello Apple Network"))

# #Oson-3. findElements(myList) - bu funksiya berilgan myList dan yoq bolgan sonlarni listini return qilsin.
# Masalan: [6, 5, 9, 3, 1] -> [2, 4, 7, 8]

# def findelements(myList):
#     return [i for i in range(1, max(myList)) if i not in myList]
#
#
# print(findelements([6, 4 ,5, 9, 13, 2]))

# #Oson-4. removeElement(myList, elem)-berilgan myList dan elem ni o'chirib tashlang.

# def removeElement(myList, elem):
#     if elem in myList:
#         myList.remove(elem)
#     return myList
#
#
# print(removeElement([6, 5, 9, 3, 1], 3))

# #Oson-5. findWeekDay(orderNumber) - bu funksiya berilgan orderNumber, yani hafta kuni
# tartibini beradi. Shu tartib boyicha hafta kunini string korinishda return qiling.
# Masalan: orderNumber = 4 Natija: Payshanba

# def findWeekDay(orderNumber):
#     weeks = ['Dushanba', 'Seshanba', 'Chorshanba', "Payshanba", 'Juma', "Shanba", "Yakshanba"]
#     if orderNumber > len(weeks):
#         return "Bunday hafta yo'q-ku!"
#     return weeks[orderNumber - 1]
#
#
# print(findWeekDay(4))

# #Oson-6. funcNumber(myList) - myList da musbat va manfiy sonlar berilgan.
# qaysi turdagi sonlar soni ko'pligini print qiling.

# def funcNumber(mylist):
#     odd = list(filter(lambda x: x >= 0, mylist))
#     even = list(filter(lambda x: x < 0, mylist))
#     return "musbat" if len(odd) > len(even) else "manfiy" if len(odd) < len(even) else "teng"
#
#
# print(funcNumber([5, -7, 3, 8, 4, -9, -2, -1, 6, 54]))

# #O'rta-1
# stringList(myList) - myList stringlar listini
# Masalan: ["Python", "Hello", "World", "Good"]
# Toq o'rindagi elementlarni toq va juft indexdagi harflarni o'rnini alishtiring.
# Masalan: "Python" -> "yPhtno"
# Juft o'rindagi elemetnlarni esa birinchi harifini oxirgisi bilan ikkinchisini oxirgisidan bitta oldingisi bilan alishtiring.
# Masalan: "Good" -> "dooG"

# def stringList(myList):
#     for i in range(0, len(myList), 2):
#         t_list = list(myList[i])
#         end_letter = ""
#         if len(t_list) % 2 == 1:
#             end_letter += t_list.pop()
#         for t in range(0, len(t_list), 2):
#             t_list[t], t_list[t + 1] = t_list[t + 1], t_list[t]
#         myList[i] = "".join(t_list) + end_letter
#
#     for j in range(1, len(myList), 2):
#         j_list = list(myList[j])
#         j_list[0], j_list[-1] = j_list[-1], j_list[0]
#         myList[j] = "".join(j_list)
#     return myList
#
#
# print(stringList(["Python", "Hello", "World", "Good"]))

# #Qiyin-1. [1, 2, 3, 4] -> [(1, 2, 3), (2, 3, 4), (1, 2, 4), (1, 3, 4))]
# findTriples(myList) - berilgan listdan bir biri bilan duch kelgan uchtalikni yangi listga append qilsin va listni return qilsin.
# (1, 2, 4) -> (2, 1, 4) mumkin emas.

# from itertools import combinations


# def findTriples(myList):
#     return [i for i in combinations(myList, 3)]
#
#
# print(findTriples([1, 2, 3, 4]))


# #Qiyin-2. moveZero(myList) - bu funksiya berilgan listdan nollarni oxiriga surib
# qolgan sonlarni o'sish tartibida tartiblaydi va yangilangan listni return qiladi.
# Masal: [5, 0, 1, 4, 0, 7, 2, 0] -> [1, 2, 4, 5, 7, 0, 0, 0]


# def moveZero(myList):
#     zero_list = [[i, myList.remove(i)][0] for i in myList if i == 0]
#     return sorted(myList) + zero_list
#
#
# print(moveZero([5, 0, 1, 4, 0, 7, 2, 0]))
# assert moveZero([5, 0, 1, 4, 0, 7, 2, 0]) == [1, 2, 4, 5, 7, 0, 0, 0]
# assert moveZero([2, 5, 6, 0, -3, 0, 56, 0, 9]) == [-3, 2, 5, 6, 9, 56, 0, 0, 0]

# #Qiyin-3. pairCount(word) - word ni ichida hamma uchrashgan jufliklarni sonni
# aniqlang va return qiling.
# Masalan: "ababwertre" -> {"ab": 3, "bw": 1, "we": 1, "er": 2, "rt": 2}


# def pairCount(word):
#     evens_list = []
#     evens_count = {}
#     for i in range(len(word) - 1):
#         evens_list.append(word[i] + word[i + 1])
#     for i in range(len(evens_list)):
#         if evens_list[i][::-1] in evens_count:
#             continue
#         if evens_list[i][0] == evens_list[i][1]:
#             evens_count[evens_list[i]] = evens_list.count(evens_list[i])
#             continue
#         evens_count[evens_list[i]] = evens_list.count(evens_list[i]) + evens_list.count(evens_list[i][::-1])
#     return evens_count
#
#
# print(pairCount("ababwertre"))
# print(pairCount("ghjkhguifdkhhksees"))
# print(pairCount("ejsavffvqwihasqv"))
#
# assert pairCount("ababwertre") == {"ab": 3, "bw": 1, "we": 1, "er": 2, "rt": 2}
# assert pairCount("ghjkhguifdkhhksees") == {'gh': 2, 'hj': 1, 'jk': 1, 'kh': 3, 'gu': 1, 'ui': 1, 'if': 1, 'fd': 1, 'dk': 1, 'hh': 1, 'ks': 1, 'se': 2, 'ee': 1}
# assert pairCount("ejsavffvqwihasqv") == {"ej": 1, "js": 1, "sa": 2, "av": 1, "vf": 2, "ff": 1, "vq": 2, "qw": 1, "wi": 1, "ih": 1, "ha": 1, "sq": 1}

# #Qiyin-4. Ikki o'lchovli list berilgan.
# Masalan: [
#   [4, 9, 3],
#   [5, 2, 6],
#   [8, 1, 7]
# ]
# Funksiya elon qiling diagonal(myList, is_reversed)
# myList - ikki o'lchovli list
# is_reversed - boolean
# Agar is_reversed = False bolsa
# Ikki o'lchovli listni to'gri diagonalini,
# is_reversed = True bo'lsa teskari diagonalini
# print qiling.
# Natija: To'gri diagonal = [4, 2, 7], Teskari diagonal = [3, 2, 8]

# #chala bo'lsa ham shartga to'g'ri keldi
# def diagonal(myList, is_reversed):
#     if is_reversed:
#         return [myList[0][0], myList[1][1], myList[2][-1]]
#     return [myList[0][-1], myList[1][1], myList[2][0]]
#
#
# example = [
#     [4, 9, 3],
#     [5, 2, 6],
#     [8, 1, 7]
# ]
# print(diagonal(example, True))
# print(diagonal(example, False))
