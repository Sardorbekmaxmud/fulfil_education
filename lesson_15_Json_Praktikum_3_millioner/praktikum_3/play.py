import json
from command_first import command_one_run_game
from command_second_rating import users_rating


def user_command_input_print():
    """Foydalanuvchi bilan ishlaydigan funksiya.
       Foydalanuvchidan buyruqni qabul qilib return qiladi"""
    user_command = input("""\33[96mKim millioner bo'lishni istaydi o'yiniga xush kelibsiz!
       Buyruqni tanlang:
       1 - o'ynash
       2 - reyting

       0 - dasturdan chiqish\n       \033[0m""")  # 0 - dasturdan chiqish\n\t   """)  # # qo'shimcha
    return user_command


def play():
    while True:
        user_command = user_command_input_print()
        if user_command == "1":
            command_one_run_game()
        elif user_command == "2":
            users_rating()
        elif user_command == "0":
            break
        else:
            print("\033[31mXato buyruq kiritdingiz!\033[0m")
            continue

play()
