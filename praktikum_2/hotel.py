hotel_users2dict = [
    {"name": "John", "room": 12, "romm_type": "standard"},
    {"name": "Doe", "room": 15, "romm_type": "standard"},
]

room_type = {"e": "ekonom", "s": "standard", "l": "lyuks"}


def print_button():
    print(
        "Astrum mehmonxonasiga xush kelibsiz!\n Buyruqni tanlang:\n 1 - mehmon qo'shish\n 2 - mehmonni ro'yxatdan chiqarish\n 3 - mehmonlar ro'yxati\n\n 0 - dasturdan chiqish")
    while True:
        try:
            user_button = int(input())
            return user_button
        except:
            "Bunday buyruq yo'q"


def button_operations(user_button):
    if user_button == 1:
        while True:
            user_name = input("Ism: ").title()
            if len(user_name) > 20:
                print("Bunday ism bo'lishi mumkin emas")
                continue
            else:
                break

        while True:
            try:
                user_room = int(input("Xona raqamini kiriting: "))
            except:
                print("Xona raqamini kiritmadingiz!")
                continue
            for i in hotel_users2dict:
                if user_room in i.values():
                    print("Bu xona band, boshqa xona tanlang")
                    break
            else:
                break

        while True:
            try:
                user_room_status = input(
                    "Xona turini quyidagi belgilar orqali tanglang:\n e - ekanom\n s - standart\n l - lyuks\n")
                if user_room_status == "e" or user_room_status == "s" or user_room_status == "l":
                    break
            except:
                print("Faqat belgilardan birini tanlang!")
                continue

        hotel_users2dict.append({"name": user_name, "room": user_room, "room_type": room_type[user_room_status]})
        print(f"{user_name} ro'yxatga qo'shildi\n\n")

    elif user_button == 2:
        sign = True
        while sign:
            if len(hotel_users2dict) == 0:
                print("Mehmonxona ro'yxati bo'sh!\n")
                break
            user_name = input("Kim mehmonxonadan ketmoqchi? ").title()
            count = -1
            for i in hotel_users2dict:
                count += 1
                if user_name in i.values():
                    del hotel_users2dict[count]
                    print(f"{user_name} Ro'yxatdan chiqarildi")
                    sign = False
                    break
            else:
                print(f"{user_name} ro'yxatda yo'q!")

    elif user_button == 3:
        print("Ismi                Xonasi                    Xona turi\n")

        for i in hotel_users2dict:
            length_name = len(list(i.values())[0])
            length_room_word = len(str(list(i.values())[1]))
            print(
                f"""{str(list(i.values())[0])}{" " * (20 - length_name)}{str(list(i.values())[1])}{" " * (26 - length_room_word)}{list(i.values())[2]}""")
        print("\n\n")

    else:
        return

# def run():
#     while True:
#         user_button = print_button()
#         if user_button == 0:
#             break
#         button_operations(user_button)
#
#
# run()