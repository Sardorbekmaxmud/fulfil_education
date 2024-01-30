# # n, counter = 5, 0
# #
# # for _ in range(n):
# #     n-=1
# #     counter+=1
# #     print(n,counter)
#
# # print(n)
# # print(counter)
#
# # from decorators_real_python import decorator as dec
# import functools
# import time
#
#
# # @dec.do_twice
# # def say_whee():
# #     print("Whee!")
# #
# #
# # # say_whee()
# #
# #
# # @dec.do_twice
# # def greet(name):
# #     print(f"Hello {name}")
# #
# #
# # # greet("Steven")
# #
# #
# # @dec.do_twice
# # def return_greeting(name):
# #     print("Creating greeting")
# #     return f"Hi {name}"
# #
# #
# # # print(return_greeting("Jeck"))
# # # help(return_greeting)
# #
# # # print(say_whee)
# # #
# # # print(say_whee.__name__)
# # #
# # # help(say_whee)
# #
# #
# # @dec.timer
# # def wrapper_some_time(num_times):
# #     for _ in range(num_times):
# #         sum(i ** 2 for i in range(10000))
# #
# #
# # # wrapper_some_time(999)
# #
# #
# # @dec.debug
# # def make_greeting(name, age=None):
# #     if age is None:
# #         return f"Assalomu alaykum, {name}!"
# #     else:
# #         return f"Vav {name}!, Siz allaqachon {age} yoshdasiz!"
# #
# #
# # # print(make_greeting("Erkin"))
# # # print(make_greeting("Furqat", age=23))
# #
# #
# # @dec.slow_down
# # def countdown(from_number):
# #     if from_number < 1:
# #         print("Ko'tarilish")
# #     else:
# #         print(from_number)
# #         countdown(from_number - 1)
# #
# #
# # # countdown(3)
#
#
#



salom = "Hello"
yangicha_salom = salom[-1]+salom[1:-1]+salom[0]
print(yangicha_salom)
