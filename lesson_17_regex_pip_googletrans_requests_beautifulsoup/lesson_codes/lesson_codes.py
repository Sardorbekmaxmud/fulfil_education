# import re
# from googletrans import Translator

# string = "My name is Sardorbek. I'm 21 years old. I'm a Student."

# check = re.search("\s", string)
# check_2 = re.findall("\s", string)

# print("Matndan qidirilgan belgining indeksi:", check.start(), "ga teng")
# print(check_2)

# text_split = re.split("\s", string)
# text_split_2 = re.split("\s", string, 2)
# print(text_split)  # barchasini split qilish
# print(text_split_2)  # split qilish chegaralangan

# sub_text = re.sub("\s", "7", string)  # hammasini joyini almshtirish
# sub_text_2 = re.sub("\s", "7", string, 3)  # almashtirishni cheklash
# print(sub_text)
# print(sub_text_2)


# search = re.search("I'm", string)
# # print(re)
# print(search)
# print(search.span())  # qidirilgan matn joylashgan indeksi --> (22, 25)
# print(search.string)  # regex ga berilgan to'liq matn --> My name is Sardorbek. I'm 21 years old. I'm a student.
# print(search.group())  # matndan qidirilgan so'z yoki belgi --> I'm

# findall = re.findall("I'm", string)
# print(findall)

# print(re.search(r"S\w+", string))
# print(re.search(r"\bS\w+", string))

# matn = "Hi, my name is Doston. My phone numbers: +998913451234 and +998885551234 +99843"

# # print(re.search("^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$", matn))
# # print(re.findall("^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$", matn))

# phone = re.findall(r"[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}", matn)
# print(phone)

# ------------googletrans---------------------------------------
# tarjimon = Translator()
#
# ozbek_matn = "Mening birinchi tarjima qilinayotgan jumlam"
#
# translate_english = tarjimon.translate(ozbek_matn, dest="kk")
# print(translate_english.text)
# translate_english_2 = tarjimon.translate(ozbek_matn, dest="ky")
# print(translate_english_2.text)


# SPECIAL_CASES = {
#     'ee': 'et',
# }
#
# LANGUAGES = {
#     'af': 'afrikaans',
#     'sq': 'albanian',
#     'am': 'amharic',
#     'ar': 'arabic',
#     'hy': 'armenian',
#     'az': 'azerbaijani',
#     'eu': 'basque',
#     'be': 'belarusian',
#     'bn': 'bengali',
#     'bs': 'bosnian',
#     'bg': 'bulgarian',
#     'ca': 'catalan',
#     'ceb': 'cebuano',
#     'ny': 'chichewa',
#     'zh-cn': 'chinese (simplified)',
#     'zh-tw': 'chinese (traditional)',
#     'co': 'corsican',
#     'hr': 'croatian',
#     'cs': 'czech',
#     'da': 'danish',
#     'nl': 'dutch',
#     'en': 'english',
#     'eo': 'esperanto',
#     'et': 'estonian',
#     'tl': 'filipino',
#     'fi': 'finnish',
#     'fr': 'french',
#     'fy': 'frisian',
#     'gl': 'galician',
#     'ka': 'georgian',
#     'de': 'german',
#     'el': 'greek',
#     'gu': 'gujarati',
#     'ht': 'haitian creole',
#     'ha': 'hausa',
#     'haw': 'hawaiian',
#     'iw': 'hebrew',
#     'he': 'hebrew',
#     'hi': 'hindi',
#     'hmn': 'hmong',
#     'hu': 'hungarian',
#     'is': 'icelandic',
#     'ig': 'igbo',
#     'id': 'indonesian',
#     'ga': 'irish',
#     'it': 'italian',
#     'ja': 'japanese',
#     'jw': 'javanese',
#     'kn': 'kannada',
#     'kk': 'kazakh',
#     'km': 'khmer',
#     'ko': 'korean',
#     'ku': 'kurdish (kurmanji)',
#     'ky': 'kyrgyz',
#     'lo': 'lao',
#     'la': 'latin',
#     'lv': 'latvian',
#     'lt': 'lithuanian',
#     'lb': 'luxembourgish',
#     'mk': 'macedonian',
#     'mg': 'malagasy',
#     'ms': 'malay',
#     'ml': 'malayalam',
#     'mt': 'maltese',
#     'mi': 'maori',
#     'mr': 'marathi',
#     'mn': 'mongolian',
#     'my': 'myanmar (burmese)',
#     'ne': 'nepali',
#     'no': 'norwegian',
#     'or': 'odia',
#     'ps': 'pashto',
#     'fa': 'persian',
#     'pl': 'polish',
#     'pt': 'portuguese',
#     'pa': 'punjabi',
#     'ro': 'romanian',
#     'ru': 'russian',
#     'sm': 'samoan',
#     'gd': 'scots gaelic',
#     'sr': 'serbian',
#     'st': 'sesotho',
#     'sn': 'shona',
#     'sd': 'sindhi',
#     'si': 'sinhala',
#     'sk': 'slovak',
#     'sl': 'slovenian',
#     'so': 'somali',
#     'es': 'spanish',
#     'su': 'sundanese',
#     'sw': 'swahili',
#     'sv': 'swedish',
#     'tg': 'tajik',
#     'ta': 'tamil',
#     'te': 'telugu',
#     'th': 'thai',
#     'tr': 'turkish',
#     'uk': 'ukrainian',
#     'ur': 'urdu',
#     'ug': 'uyghur',
#     'uz': 'uzbek',
#     'vi': 'vietnamese',
#     'cy': 'welsh',
#     'xh': 'xhosa',
#     'yi': 'yiddish',
#     'yo': 'yoruba',
#     'zu': 'zulu',
# }


# -==-=-=-============----requests and beautifulsoup----------------
# import requests
# from bs4 import BeautifulSoup

# from googletrans import Translator

# tarjimon = Translator()


# soup = BeautifulSoup(request_daryo.text, 'html.parser')
# news = soup.find_all(class_="is-title post-title")
# for new in news:
# print(new.text)

#
# request = requests.get("https://kun.uz/news/list")
# soup = BeautifulSoup(request.text, 'html.parser')
# news = soup.find_all(class_="news-title")
# for new in news:
#     print(new.text)
# en = tarjimon.translate(news[1].text, dest='en').text
# # print(en)
# print(tarjimon.translate(en, dest="uz", src="en").text)


# ##-=--------------------------------====================================

# import re
#
# matn = "Are you writing python code? Yes I'm. And you?"
#
# check = re.search(r"you", matn)
# print(check)  # <re.Match object; span=(4, 7), match='you'>
# print(check.group())  # izlanayotgan so'z
# print(check.span())  # topilgan so'z indekslari oralig'i
# print(check.string)  # izlash uchun matn
#
# check_find_all = re.findall("you", matn)  # --> ['you', 'you']
# print(check_find_all)  # matn dan qidirilgan so'z ning topilgan ro'yxati
#
# data = "My all phone numbers: 998331234567, 786-307-3615  +998715633421 and +17312353513"
# findall_phone = re.findall(r"[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}", data)
# search_phone = re.search("[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}", data)
#
# print(findall_phone)  # to'g'ri formatdagi barcha tel raqamlar
# print(search_phone)  # birinchi topilgan tel raqam
#
# reverse_or_sub_text = re.sub(r"A", "\a", matn)  # \a == 
# print(reverse_or_sub_text)  # o'rnini almashtirish
#
#
# split_text_in_regex = re.split("\s", matn)
# print(split_text_in_regex)  # str dagi split metodi bilan 1 xil
#
#
# text = "I'm 23 years old. Men 2000 yilda tug'ilganman."
# print(re.findall(r"\d", text))
#
# t = "The 5 cats ate 12 Angry men"
# print(re.findall(r"\D", t))


# -===========================================
# from googletrans import Translator
#
# tarjimon = Translator()
#
# uzbek_matn = "javascriptda matnlar bilan ishlash uchun methods"
#
# en_text = tarjimon.translate(uzbek_matn, dest="en").text
# print(en_text)


# from googlesearch import search
#
# your_text = "install gtts package"
#
# for i in search(your_text, tld="co.in", num=10, stop=10, pause=2):
#     print(i)

# from gtts import gTTS
# import os
#
# your_text = ""
#
# my_first_speak_in_laptop = gTTS(text=your_text, lang='en', slow=True)  # slow = tezligi
#
# my_first_speak_in_laptop.save("speak_in_my_laptop.mp3")
#
# os.system("speak_in_my_laptop.mp3")

#
# # for j in search(en_text, tld="co.in", num=10, stop=10, pause=2):
# #     print(j)


# import requests
# from bs4 import BeautifulSoup
#
# response = requests.get("https://daryo.uz/yangiliklar")
# # print(response.text)
# soup = BeautifulSoup(response.text, "html.parser")
# news = soup.find_all(class_="is-title post-title limit-lines l-lines-3")
# c = 0
# for new in news:
#     print(new.text, end="")

# from googlesearch import search
#
# for text in search(query="Neymar Amerika Kubogi—2024 musobaqasini o‘tkazib yuboradi", num=3, stop=3):
#     print(text)


# from http import HTTPStatus
# print(HTTPStatus.OK)

#
# from googletrans import Translator
# from gtts import gTTS
# import os
#
# tarjimon = Translator()
#
# ozbekcha_sher_matni = """
# Oftob chiqdi olamga,
# Yugurib bordim holamga.
# -Xola,xola kulcha ber!
# Holam dedi: -O’tin ter!
#
# O’tin terdik bir quchoq.
# Sezmadik sira charchoq!
# Xolam yopdi kulcha non.
# Non isiga to’ldi xar yon!
# """
#
# en_text = tarjimon.translate(ozbekcha_sher_matni)
# print(en_text.text, "\n")
# print(tarjimon.translate(en_text.text, dest='uz', src="en").text)
#
# oftob_chiqdi_sheri_inglizcha = gTTS(text=en_text.text)
#
# oftob_chiqdi_sheri_inglizcha.save("inglizcha_ofton_chiqdi_sheri.mp3")
#
# os.system("inglizcha_ofton_chiqdi_sheri.mp3")
