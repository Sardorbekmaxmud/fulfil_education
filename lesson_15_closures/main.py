# a = 3
#
#
# def f1():
#     return a
#
#
# def f2():
#     global a  # asl >>a<< yani 1 qatordagi a ni o'zi
#     a += 2
#     return a


# print(a, id(a))
# print(,id(f2()))
# f2()
# print(a, id(a))


# def p():
#     a = 3
#     print(id(a))
#     def f():
#         nonlocal a
#         print(id(a))
#         a+=4
#         print(id(a))
#         return a
#     return f

# pa = p()
# print(pa())
# print(pa(f()))

# def parent(a):
#     def son(b):
#         return b
#     return son

# x = 5
# y = 2

# answer = parent(x)(y)
# print(answer)

# def g_father(a):
#     def father(b):
#         def son(c):
#             return c
#         return son
#     return father
#
# x = 5
# y = 2
# z = 0
#
# answer = g_father(x)(y)(z)
# print(answer)

# def parent(a):
#     c = 8
#     def son(b):   # son hali closures emas
#         return c * (a+b)
#     return son

# x = 5
# y = 2

# t = parent(x)
# i = t(y) # endi closures bo'ldi negaki u son ga teng bo'ldi

# print(i)

# print(t.__code__.co_freevars) #  free variablelarni ko'rish uchun ular a, b
# print(t.__closure__[0].cell_contents)  # qiymatlarini ko'rish 0 hozir a ning qiymatiga teng
# print(t.__closure__[1].cell_contents) # qiymatlarini ko'rish 1 hozir b ning qiymatiga teng

# def f(x):
#     z = 4
#     def g(y):
#         return y
#     return g

# a, b = 2, 6
# h = f(a)
# i = h(b)
# print(h.__code__.co_freevars)

# def f(a):
#     def g(b): # bu yerda g func -->> a <<-- ni o'tkazib bera yotgani uchun bu ham closures
#         def v(c): # bu ham closures
#             return a * b * c
#         return v
#     return g

# x, y, z = 7,2,3
# pr = f(x)
# sn = pr(y)
# ans = sn(z)

# print(ans)

# print(pr.__code__.co_freevars,end=' == ')
# print(pr.__closure__[0].cell_contents)

# print(sn.__code__.co_freevars)
# print(sn.__closure__[0].cell_contents)
# print(sn.__closure__[1].cell_contents)

# def f(x):
#     z = 5
#     return lambda y: x * y * z

# sn = f(3)
# ans = sn(6)
# print(ans)

# m_to_sm = lambda x: x*100
# km_to_m = lambda x: x*1000
#
# def compose(a, b):
#     def h(*args,**kwargs):
#         return b(a(*args,**kwargs))
#     return h
#
#
# km_to_sm = compose(km_to_m,m_to_sm)
#
# print(km_to_sm(12))
#
# from googlesearch import search
#
# for i in search("python decorator",lang='en',stop=10, pause=2):
#     print(i)


# def f(x):
#     z = 2
#     def g(y):
#         return y * x * z
#     return g
# a = 5
# b = 1
# h = f(a)
# h(b)
# print(h.__code__.co_freevars)
# print(h.__closure__[0].cell_contents)
# print(h.__closure__[1].cell_contents)


