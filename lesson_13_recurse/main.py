# def countdown(n):
#     print(n)
#     if n==0: # bu shart bajarilsa rekursiv func tugaydi
#         return
#     else:
#         countdown(n-1)

# countdown(5)

# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(500))


# def fibonacci(n,cache={}):
#     if n in cache:
#         return cache[n]
#     if n==0:
#         return 0
#     elif n==1:
#         return 1
#     else:
#         result =  fibonacci(n-1) + fibonacci(n-2)
#     cache[n] = result
#     return result

# print(fibonacci(4))

# def quick_sort(lst):
#     if len(lst)<=1:
#         return lst
#     else:
#         first_num = lst[0]
#         left = [i for i in lst[1:] if i <= first_num]
#         right = [i for i in lst[1:] if i > first_num]
#         return quick_sort(left) + [first_num] + quick_sort(right)

# print(quick_sort([5,7,2,0,3,1,6]))


# -=-=-=-=-=-=-=-=-=-=-=-=qayta yechim-=-=-=-=--=-=-=-=-=--=-=-=--=-=-=-=-=-=-=-=--=
# def countdown(n):
#     print(n)
#     if n == 0: # Base condition
#         return
#     else:
#         countdown(n-1) # recursive call
#
# countdown(5)

# def factorial(x):
#     if x == 0:
#         return 1 # base condition -->> chiqish eshigi
#     else:
#         return x * factorial(x-1) # recursive call -->> rekursiyaga murojaat
#
# print(factorial(5))

# def factorial(x,cash={}):
#     if x in cash:
#         return cash[x]
#     if x == 0:
#         result = 0
#     elif x == 1:
#         result = 1
#     else:
#         result = factorial(x-1) + factorial(x-2)
#     cash[x] = result
#     return result
# print(factorial(20))


def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        first_num = lst[0]
        left = [i for i in lst[1:] if i <= first_num]
        right = [i for i in lst[1:] if i > first_num]
        return quick_sort(left) + [first_num] + quick_sort(right)


print(quick_sort(lst=[4, 6, 8, 3, 5, 7, 2, 0, 3, 1, 6, 1, 7, 12, 1]))


# lst = [4, 6, 8, 3, 5, 7, 2, 0, 3, 1, 6, 1, 7, 12, 1]
# lst.sort()
# print(lst)
