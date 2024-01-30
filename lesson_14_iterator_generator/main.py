# mylist = [1,2,3]
# mylist_iter = iter(mylist)
import math

# print(type(mylist))
# print(type(mylist_iter))

# print(next(mylist_iter))
# print(next(mylist_iter))
# print(next(mylist_iter))

# while True:
#     try:
#         print(next(mylist_iter))
#     except StopIteration:
#         break

# f = open(file='t.csv')

# print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))

# class Counter:
#     def __init__(self, low, high):
#         self.current = low - 1
#         self.high = high

#     def __iter__(self):
#         return self

#     def __next__(self):
#         self.current += 1
#         if self.current < self.high:
#             return self.current
#         raise StopIteration

# for elem in Counter(1, 10):
#     print(elem)

# def try_generator(y):
#     n = y
#     n+=1
#     print('chiqarish')
#     yield n

#     n*=2
#     print('next print')
#     yield n

# result = try_generator(5)
# print(next(result))
# print(next(result))


# #kiritilgan min va max sonlari oralig'idagi sonlar kvadratga oshirib faqat chaqilganda return qiluvchi funk.
# def return_squared(min,max):
#     for i in range(min,max+1):
#         yield i**2
#
# result = return_squared(1,5)
#
# for kvadrat in result:
#     print(kvadrat)


# # bu oddiy list comprehension. birdan hamma listdagi elementlarni chiqaradi -> [0, 1, 2, 3, 4]
my_list_num = [i for i in range(5)]
print(my_list_num)


# #bu Anonim generator. Generator qaytaradi. Bu faqat chaqirsagini elementni ko'rsa bo'ladi.
my_list_num_gen = (i for i in range(5))
print(my_list_num_gen) # <generator object <genexpr> at 0x000001E30ECAFED0>
for i in my_list_num_gen:
    print(i)
# # 0 1 2 3 4

# # -=-=-=-======-=-==-=-qayta yechim uyga vazifa=-=-=-=-=-=-==-=--=-=-=-=-=-=--=-=-=

# # 1 tub sonlar generator qiluvchi funksiya yasash
# def GeneratorPrimeNumber():
#     def is_prime(n):
#         n_ildiz = int(n ** 0.5)
#
#         for i in range(2, n_ildiz + 1):
#             if n % i == 0:
#                 return False
#         return True
#
#     i = 2
#     while True:
#         if is_prime(i):
#             yield i
#             i += 1
#         else:
#             i += 1
#
#
# result = GeneratorPrimeNumber()
#
# for i in range(14):
#     print(next(result))

# # 2 kiritilgan matndan parol generatsiya qiladigan funksiya.
import itertools


# def password_generator(string):
#     for i in itertools.permutations(string):
#         yield ''.join(i)
#
#
# text = input("So'z yoki matn kiriting: ")
# result = password_generator(text)
#
# for i in range(6):
#     try:
#         print(next(result))
#     except StopIteration:
#         break

# # 3 cheksiz fibonachchi sonlarini generator qiladigan generator funsiya
# def fibonacci():
#     a, b = 0, 1
#     fib_numbers = [a, b]
#     while True:
#         yield a
#         a, b = a + b, fib_numbers[-1]
#         fib_numbers.append(a)
#
#
# result = fibonacci()
#
# for i in range(10):
#     print(next(result))

# # 4 chala ku lekin ishlaydi 2 talab guruhlasa
# def group_generator(my_list, n):
#     length_list = len(my_list)
#     for i in range(1, length_list + 1):
#         for j in range(i, length_list + 1):
#             if my_list[i - 1] == my_list[j - 1]:
#                 continue
#             yield my_list[i - 1], my_list[j - 1]


# result = (group_generator([1, 2, 3, 4], 2))

# while True:
#     try:
#         print(next(result), "->", end=' ')
#     except StopIteration:
#         break

# def group_generator(lst, n):
#     for i in itertools.combinations(lst, n):
#         yield i
#
#
# my_list = [1, 2, 3, 4, 5, 6, 11]
# n =
# result = group_generator(list(set(my_list)), n)
#
# for _ in range(17):
#     try:
#         print(next(result))
#     except StopIteration:
#         break



# #-=-=-=-=-=-=-=-=-=-=-Mavzudan, darsdan tashqaridagi misol-=-=-=--=-=-=-=-=-=-=-=-=-==-==-=-==-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=
# #Bu funksiya kiritilayotgan parametr fibonacci sonmi yoki yo'qligini qaytaruvchi funksiya.
# def is_fibonacci(n):
#     a, b = 0, 1
#     while True:
#         if a == n or b == n:
#             return True
#         a, b = b, a + b
#         if a > n:
#             return False


# n = int(input("son: "))
# print(is_fibonacci(n))
# def test():
#     assert is_fibonacci(0) == True
#     assert is_fibonacci(1) == True
#     assert is_fibonacci(2) == True
#     assert is_fibonacci(13) == True
#     assert is_fibonacci(55) == True
#     assert is_fibonacci(78) == True
#
#     print("Success")


# test()
