# # 1 append() list metodi.U listnig oxiriga 1 ta element qo'shadi
# sonlar = [23,7,23,0,1,7,2,5]
# print(sonlar)
# sonlar.append(8)
# print(sonlar)

# # 2 extend() list metodi. u listning oxiriga 1 nechta element qo'sha oladi,faqat list,tuple,set or (dict faqat keys larni oladi) da elementlarni qo'shish kerak
# mevalar = ["gilos","behi","nok","limon","apelsin"]
# print(mevalar)
# mevalar.extend(("olma",123,"olxo'ri"))
# print(mevalar)

# # 3 clear() list metodi list butunlay tozalaydi
# citys = ["Tashkent","Almata"]
# citys.clear()
# print(citys)

# # 4 copy() list metod. listni nusxalash uchun kerak
# cars = ["audi",'bmw','hyundai']
# cars2 = cars.copy()
# cars2.append("jeep")
# print(cars)
# print(cars2)

# # 5 listdagi elementlarni sonini sanaydi. count() metodi
# laptops = ["asus",'hp',"acer","apple","asus"]
# print(laptops.count("asus"))

# # 6 index() metodi listdagi element qaysi indexda turganligini aytadi
# countrys = ["Uzbekistan","USA","Russia","India","China"]
# print(countrys.index('USA'))

# # 7 insert() metodi listning hohlagan joyiga element qo'shsa bo'ladi
# books = ["Shaytanat","Pythonda dasturlash asoslari"]
# books.insert(1,"Million dollarlik xatolar")
# print(books)

# # 8 pop() metodi listning hohlagan joyidan elementni sug'urib oladi va uni bironta o'zgaruvchi yuklasa bo'ladi,sug'urib olish un indexni berish kk yoki bermasa oxiridan oladi
# numbers = [4,6,7,12,74,234,0,44,-5]
# num = numbers.pop(1)
# print(num)
# print(numbers)

# # 9 listdan bironta elementni o'chirish uchun remove() metodi ishlatiladi.
# rivers = ["sirdaryo","ob",'volga','nil','volga']
# rivers.remove('volga')
# rivers.remove('volga')
# print(rivers)

# # 10 listni teskari o'girib beradi reverse() metodi printda qo'llab bo'lmaydi
# ismlar = ["firdavs","olim",'zafar','shovkat','xurshid','komil']
# ismlar.reverse()
# print(ismlar)

# # 11 listdagi elementlarni alifbo yoki sonlarni boshidan tartiblab beradi
# daraxtlar = ["terak","olcha","behi",'mejnun tol',"abrikos"]
# daraxtlar.sort(reverse=True)
# daraxtlar.sort(key=len)
# print(daraxtlar)
#
# def myFunc(e):
#   return len(e)

# cars = [
#   {'car': 'Ford', 'year': 2005,'price':10000000},
#   {'car': 'Mitsubishi', 'year': 2000,'price':12300000},
#   {'car': 'BMW', 'year': 2019,'price':6357982}
# ]

# cars.sort(key=lambda x: x['year'])
# print(cars)
# cars.sort(key=lambda x: x['car'])
# print(cars)
# cars.sort(key=lambda x: x['price'],reverse=True)
# print(cars)


