# # # 1
# def generator_tub_num():
#     def is_tub(num):
#         for i in range(2,int(num**0.5)+1):
#             if num%i==0:
#                 return False
#         return True

#     number = 2
#     while True:
#         if is_tub(number):
#             yield number
#         number+=1

# start_func = generator_tub_num()

# for _ in range(8):
#     print(next(start_func))


# # 2
# import itertools
# user_str = input("So'z kiriting: ")

# def generate_password(word):
#     for i in itertools.permutations(word):
#         yield ''.join(i)

# for i in generate_password(user_str):
#     print(i)

# # 3 cheksiz generator qiluvchi funksiya.
# def generate_fibonacci_num():
#     f,s=0,1
#     a=[f,s]
#     while True:
#         yield f
#         f,s = s,f+s
#     # i=0
#     # while True:
#     #     yield a[i]
#     #     a.append(a[i]+a[i+1])
#     #     i+=1
#
# result = generate_fibonacci_num()

# for _ in range(10):
#     print(next(result))

# # 4 listning elementlarini n (masalan: 3) nechiligi  qarab guruhlab beruvchi funksiya.
# import itertools
# def generate(l,n):
#     for i in itertools.combinations(l,n):
#         yield i

# answer = generate([1,2,3,4],3)

# for i in answer:
#     print(i)
