# def deco(funksiya):
#     def inner_func(*args,**kwargs):
#         print(f"Func name: ",funksiya.__name__)
#         return funksiya(*args,**kwargs)
#     return inner_func

# @deco
# def name_print_and_age(age):
#     print(f"Sardorbek {age} age")

# # name_print_and_age = deco(name_print_and_age) 👈 == 👉 @deco
# name_print_and_age(21)

# def main(inn):
#     def inner(n):
#         print('function name: ',inn.__name__)
#         return inn(n)
#     return inner

# @main
# def local(name):
#     print('Hello',name)

# local('Sardorbek')


# for i in range(5):
#     print(fib(i),end=' ')

# def fib(num):
#     if num==0:
#         return 0
#     elif num==1:
#         return 1
#     else:
#         return fib(num-1) + fib(num-2)

# def memoisation_func(parametr):
#     memo = dict()
#     def inner_func(num):
#         if num not in memo:
#             memo[num] = parametr(num)
#         # print(memo)
#         return memo[num]
#     return inner_func

# fib = memoisation_func(fib)
# print(fib(30))

# -------------HOMEWORK FOUR example---------------------

# # 1 matnni katta qilib beruvhci decorator
# def upper_deco(f):
#     def inner_func(*args,**kwargs):
#         answer = f(*args,**kwargs)
#         return answer.upper()
#     return inner_func
#
# @upper_deco
# def hello(name):
#     return f"Hello, {name}"

# print(hello('sardorbek'))

# # 2 matnni teskari qilib beruvchi decorator
# def reverse_deco(f):
#     def inner_func(*args,**kwargs):
#         answer = f(*args,**kwargs)
#         return answer[::-1]
#     return inner_func
#
# @reverse_deco
# def string(name):
#     return f"{name}"

# print(string('sardor'))

# # 3 func ishlashiga qancha vaqt ketayotganini hisoblaydi
# import time
# def time_late_deco(f):
#     def inner_func(*args,**kwargs):
#         start = time.time()
#         answer = f(*args,**kwargs)
#         end = time.time()
#         return f"{f.__name__}, {end-start:.3f}"
#     return inner_func

# @time_late_deco
# def func(str):
#     for i in range(900):
#         for j in range(i,899):
#             print("", end='   ')
#         for n in range(i):
#             print("*",end='   ')
#         for n in range(i+1):
#             print("*",end=' ')
#         print()

# print(func('sardorbek'))

# # 4  necha marta func chaqirilayotganini sanaydi
# def run_count_deco(f):
#     def inner_func(*args,**kwargs):
#         inner_func.calls+=1
#         answer = f(*args,**kwargs)
#         return inner_func
#     inner_func.calls = 0
#     return inner_func
#
# @run_count_deco
# def hello():
#     pass

# f = hello()
# s = hello()
# print(hello.calls)

# -=-=-==-=-=-=-==-=-=-QAYTA YECHIM=-=-=-=-=-=-=---=
# -=-=-==-=-=-=-==-=-=-UYGA VAZIFA 4 MISOL=-=-=-=-=-=-=---=
import functools
import time


def dec_string_upper(func):
    @functools.wraps(func)
    def inner_func_str_upper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return inner_func_str_upper


@dec_string_upper
def replace_str(string):
    return string


# print(replace_str("test uchun matn kiritildi!"))


def dec_string_reverse(func):
    @functools.wraps(func)
    def inner_func_str_upper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result[::-1]

    return inner_func_str_upper


@dec_string_reverse
def string_rever(text):
    return text


# print(string_rever("kiyik, tut, aka, 123"))


def func_count_call(func):
    @functools.wraps(func)
    def inner_func_str_upper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"{func.__name__!r} funksiyasiga {run_time:.4f} sekund ketdi!")
        return result

    return inner_func_str_upper


@func_count_call
def so_loop():
    s = [i for i in range(100000)]


# so_loop()


def dec_fun_count_run(func):
    @functools.wraps(func)
    def inner_func_str_upper(*args, **kwargs):
        inner_func_str_upper.calls += 1
        result = func(*args, **kwargs)
        return result
    inner_func_str_upper.calls = 0
    return inner_func_str_upper


@dec_fun_count_run
def greeting(name):
    return f"Hi, {name}"


# greeting("Doston")
# greeting("Doston")
# greeting("Doston")


# print(f"{greeting.__name__!r} {greeting.calls} marta ishladi.")


