# # 1
# str = "dars qilayapman pythondan"
# print(str.capitalize())

# # 2 ❗
# str_2 = "bu Yerda matn bor"
# print(str_2.casefold())

# # 3
# str_3 = "test uchun matn yozildi"
# print(str_3.center(31))
# print(str_3.center(31,"*")) # tashlanayotgan joyga * qo'yildi

# # 4 ❗
# str_4 = "dachaga borib kelish kerak"
# print(str_4.count("a"))
# print(str_4.count("a",4,18)) # oraliq bersa bo'ladi sanayotganda

# # 5 ❗
# str_5 = "1 kunda 3 ta dars ko'rdim."
# print(str_5.endswith("im."))
# print(str_5.endswith("da",3,7)) # oraliq bersa bo'ladi

# # 6
# str_6 = "\ttable tashlash\t uchun me\ttodiga yozilgan matn"
# print(str_6.expandtabs(4))

# # 7 ❗
# str_7 = "w3school string metods rini yozib ko'rayapman"
# print(str_7.find("m"))
# print(str_7.find("m",20,50)) # oraliqda qidirish uchun berib ketsa bo'ladi

# # 8 :%,  :f,  :_,  :,,  :-,  :+,  :=,  :^,  :>, :<
# str_8 = "{} daraxtlar shamolda tebranmoqda {:n}"
# print(str_8.format("uyni oldida",1200000))
# str_8 = "{1} daraxtlar shamolda tebranmoqda {0}"
# print(str_8.format(134,"uyni"))

# # 9 ❗
# str_9 = "mening ismim Sardorbek"
# print(str_9.index("e"))
# print(str_9.index("e",2,25)) # oraliqdan izlashi un bersa bo'ladi

# # 10 ❗
# str_10 = "bugun05"
# print(str_10.isalnum()) # only alifbo harflari or number or alifbo and number bo'lsa true qaytaradi

# # 11 ❗
# str_11 = "tushlukkanimayeymiz"
# print(str_11.isalpha())

# # 12
# str_12 = "hgqyt4394hei(*&" # bu str
# print(str_12.isascii()) # ascii table da bor bo'lsa true qaytaradi

# # 13
# str_13 = "17935433455678"
# print(str_13.isdecimal()) # only input int number

# # 14
# str_14 = "154135"
# print(str_14.isdigit()) # faqat sonlar va kichik ko'rinishdagi sonlar bo'lsa true qaytaradi

# # 15❗ (a-z),(0-9) and (_) bo'lsa true qaytaradi
# str_15 = "sardorbek"
# str_15_2 = "2Sardorbek"  # username number bn boshlansa bo'lmaydi
# str_15_3 = "_Sardorbek"
# str_15_4 = "Sardorbek23"
# str_15_5 = "Sardorbek_23"
# print(str_15.isidentifier())
# print(str_15_2.isidentifier())
# print(str_15_3.isidentifier())
# print(str_15_4.isidentifier())
# print(str_15_5.isidentifier()) # asosan username ga ishlatsa bo'ladi

# # 16 matndagi harflar kichik bo'lsa true qaytaradi
# str_16 = "kichkinalikni tekshirish uchun matn"
# str_16_2 = "Django Python kurs f-31"
# str_16_3 = "jevior3491304(*& "
# print(str_16.islower())
# print(str_16_2.islower())
# print(str_16_3.islower())

# # 17 faqat son, kichik son va 3/4 sonlar bo'lsa true qaytaradi
# str_17 = "15345"
# str_17_2 = "15345\u00B2"
# print(str_17.isnumeric())
# print(str_17_2.isnumeric(),str_17_2)

# # 18 ekranga str dagi hamma matn chiqsa true qaytaradi
# str_18 = "text test qilish uchun"
# str_18_2 = "text test\t qilis1973513847\#$%^h uchun"
# print(str_18.isprintable())
# print(str_18_2.isprintable())

# # 19 # matn bo'shliq bo'lsa true qaytaradi
# str_19 = "        " # True
# str_19_2 = "   e     " # False
# str_19_3 = "    \t \n    " # True
#
# print(str_19.isspace())
# print(str_19_2.isspace())
# print(str_19_3.isspace())

# # 20 # so'z boshlanishi kata hraf bo'lsa true qaytaradi.Keyingilari katta bo'lmasligi kerak son,belgilar bo'lishini farqi yo'q
# str_20 = "Qator tashlab yoz" #True
# str_20_2 = "Qator Tashlab Yoz" # True
# str_20_3 = "Qator 345 tashlab yoz%$#@" # False
# str_20_4 = "Qator,134444444 Tashlab Yoz*^&%^$%$" # True
# str_20_5 = "EKRNGA CHIQADIGAN TEXT," # False
#
# print(str_20.istitle())
# print(str_20_2.istitle())
# print(str_20_3.istitle())
# print(str_20_4.istitle())
# print(str_20_5.istitle())

# # 21 # faqat katta harflar bo'lsa true qaytaradi.son,belgilar bn ishi yo'q
# str_21 = "MATN FAQAT KATTA HARFLARDAN IBORAT"
# str_21_2 = "iuwSNFegitu"
# str_21_3 = "1234qeiurghq"
# str_21_4 = "EIFUNHQEIUR#$%^&234"
#
# print(str_21.isupper())
# print(str_21_2.isupper())
# print(str_21_3.isupper())
# print(str_21_4.isupper())

# # 22 ❗
# t = ("Anvar", "Ali","Hasan")
# str_22 = ", ".join(t)
# print(str_22)

# # 23 matn ning chap tarafidan length qarab joy tashlaydi
# str_23 = "qwertyu"
# print(str_23.ljust(8))
# print(str_23.ljust(8,"*")) # bo'sh joyga qo'ysa bo'ladi

# # 24
# str_24 = "yigirma tO'rtinchi mAtn"
# print(str_24.lower())

# # 25 # chapdan matnda joy bo'lsa olib tashlaydi
# str_25 = "       notebookda kino ko'rish ancha yaxshi     "
# print(str_25.lstrip())

# # 26 belgilarni almashtirish uchun  kerak
# str_26 = "Favvora juda ham chiroyli"
# str = "uaio" # bor harflar
# str_2 = "UAIO" # almashadigan hraflar
# str_3 = "n" # o'chiriladigan harflar
# txt = str.maketrans(str,str_2,str_3)
# print(str_26.translate(txt))

# # 27 # bu qidirish uchun, uni 3 ga bo'ladi va tuplega aylantiradi. qidirilayotgan matn bor bo'lsa matn,qidirilgan matn va undan keying matn bor bo'lsa shu matn qo'yiladi
# str_27 = "Bu yerda matn bor"
# print(str_27.partition("matn")) # ('Bu yerda ', 'matn', ' bor')
# print(str_27.partition("bor")) #  ('Bu yerda matn ', 'bor', '')
# print(str_27.partition("yo'q")) # ('Bu yerda matn bor', '', '')

# # 28 ❗ # matn ni o'zgartirish uchun metod
# str_28 = "Nodir ishlaydi,Nodir Dasturchi"
# print(str_28.replace('N','Q'))
# print(str_28.replace('N','Q',1)) # nechta matn or harfni almashtirishni bersa bo'ladi

# # 29 # matndagi eng oxirgi qidirilayotgan harf indexni qaytaradi
# str_29 = "rfind bn ishlash"
# print(str_29.rfind('n'))
# print(str_29.rfind('n',0,12)) # oraliq bersa bo'ladi

# # 30 # matndagi eng oxirgi qidirilayotgan harf indexni qaytaradi
# str_30 = "rindex metod ini qo'llab ko'rish"
# print(str_30.rindex('i'))
# print(str_30.rindex('i',7,19))

# # 31 # matn ni o'ngga surib chapdan, berilgan songa qarab joy tashlaydi
# str_31 = "olma, uzum"
# print(str_31.rjust(20))
# print(str_31.rjust(20,'*'))

# # 32
# str_32 = "shunchaki matn bor bu yerda"
# print(str_32.upper())

# # 33
# str_33 = "       notebookda kino ko'rish ancha yaxshi     "
# print(str_33.rstrip())

# # 34 ❗
# str_34 = "       notebookda kino ko'rish ancha yaxshi     "
# str_34_1 = "..so,'z kiritildi.."
# print(str_34.strip())
# print(str_34_1.strip('v .imvr')) # so'zning chetlaridan olib tashlaydi. argument qilib berilsa ham chekkasidan oladi. Agar chetidan olib kelsa ola oladi, birdan o'rtasidagini ola olmaydi.


# # 35
# str_35 = "jeklon london"
# print(str_35.title())

# # 36 ❗# matn ni list ga bo'ladi necha qismga bo'linishini ham bersa bo'ladi
# str_36 = "non,tuxum,daftar,zebra"
# print(str_36.split(','))
# print(str_36.split(',',1))

# # 38 ❗# kattani kichikka, kichikni katta almashtirish metodi
# str_38 = "tarixda o'tgan ULug' ulamolar"
# print(str_38.swapcase())

# # 39 # belgilangan uzunlikka yetmasa oldiga 0 qo'yadi
# str_39 = "hqwqer"
# str_39_2 = "hqw%#$@wghiueutgqer"
# str_39_3 = "175408"
#
# print(str_39.zfill(10))
# print(str_39_2.zfill(10))
# print(str_39_3.zfill(10))

# # 40 # \n qatnashgan joydan nechiga bo'lish kerak bo'lsa bo'ladi. listda \n bo'lmasa to'liq list bo'ladi
# str_40 = "mant bor test uchun"
# str_40_2 = "mant bor \ntest uchun"
# print(str_40.splitlines()) #default false bo'ladi
# print(str_40_2.splitlines(True)) # qo'ysa \n ham ko'rinadi

# # 41
# str_41 = "Oxirgisi. bo'ladi shunchasi!"
# ascii1 = {97:65}
# print(str_41.translate(ascii1))