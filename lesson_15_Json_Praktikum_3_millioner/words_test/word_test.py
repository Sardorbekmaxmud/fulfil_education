import json

variant_letters = ["a) ", "b) ", "c) ", "d) "]
variant_letters_check = ["a", "b", "c", "d"]


def user_command_input_print():
    """Foydalanuvchi bilan ishlaydigan funksiya.
       Foydalanuvchidan buyruqni qabul qilib return qiladi"""
    user_command = input("""\33[96mKim millioner bo'lishni istaydi o'yiniga xush kelibsiz!
       Buyruqni tanlang:
       1 - o'ynash
       2 - reyting

       0 - dasturdan chiqish\n       \033[0m""")  # 0 - dasturdan chiqish\n\t   """)  # # qo'shimcha
    return user_command


def is_user_have(name):
    """Bazada user bormi yo'qmi aniqlab
       True yoki False qaytaradi"""
    users_data = ""
    try:
        users_data = json.load(open("users.json"))
    except:
        with open("users.json", "w") as f:
            pass

    user_have = False
    for i in users_data:
        if name in i.values():
            user_have = True
            break
    if user_have:
        return user_have
    return user_have


def add_user_data(name: str, played: int, best_score: int):
    """Bazaga ma'lumot qo'shadi"""
    try:
        users_data = json.load(open("users.json"))  # bazani olib unga yangi element qo'shish uchun ochadi
        add_user = {
            "name": name,
            "played": played,
            "best_score": best_score
        }
        users_data.append(add_user)
        with open("users.json", "w") as f:  # bazaga yangi user qo'shadi
            json.dump(users_data, f, indent=4)
    except:
        with open("users.json", "w") as f:
            add_user = [{
                "name": name,
                "played": played,
                "best_score": best_score
            }]
            json.dump(add_user, f, indent=4)


def update_user_data(name: str, played: int, best_score: int):
    """Bazadagi ma'lumotni update qiladi"""
    users_data = json.load(open("users.json"))
    for i in users_data:
        """parametr sifatida kelgan name va best_score 
        baza dagi name ga teng va yuqori natijasi katta yoki teng bo'lsa ishlaydi"""
        if i['name'] == name and best_score >= i['best_score']:
            i['played'] = played
            i['best_score'] = best_score
        #  parametr sifatida kelgan name va best_score
        #  baza dagi name ga teng va yuqori natijasi katta yoki teng bo'lsa ishlaydi
        elif i['name'] == name and best_score <= i['best_score']:
            i['played'] = played
            i['best_score'] = i['best_score']

    with open("users.json", "w+") as f:
        json.dump(users_data, f, indent=4)


def win_user(question_num, player_name, user_played, true_answer_count):
    """Foydalanuvchi test ni to'liq bajara olsa,
       bazada yo'q bo'lsa qo'shadi, agar bazada bor bo'lsa yangilaydi."""
    with open("word_test.json") as f:
        tests = json.load(open("word_test.json"))
    if question_num == len(tests):
        if is_user_have(player_name) == True:
            update_user_data(name=player_name, played=user_played + 1, best_score=true_answer_count)
        else:
            add_user_data(name=player_name, played=user_played, best_score=true_answer_count)


def help_(question_num, i, count_help):
    with open("word_test.json") as f:
        datas = json.load(f)
    """Yordam funksiyasi"""
    if count_help > 3:
        print(" Siz yordamdan foydalanib bo'ldingiz.\n" + f"\033[36msavol {question_num}/{len(datas)}\033[0m\n" + i[
            'question'], "\n")
        return "stop"
    questions = []
    true_question = ""
    for k in range(4):
        if i['answers'][k]["isTrue"] == True:
            true_question = f"{variant_letters[k]}" + i['answers'][k]['key']
        else:
            questions.append((f"{k}" + i['answers'][k]['key']))
    if ord(variant_letters_check[int(questions[2][0])]) < ord(true_question[0]):
        print(
            f"  {(questions[0][1:])} va {questions[1][1:]} variantlari olib tashlandi\n" + f"\033[36msavol {question_num}/10\033[0m\n" +
            i['question'], "\n\n" + variant_letters_check[int(questions[2][0])] + ") " + questions[2][1:],
            f"\n{true_question}")
    else:
        print(
            f"  {(questions[0][1:])} va {questions[1][1:]} variantlari olib tashlandi\n" + f"\033[36msavol {question_num}/{len(datas)}\033[0m\n" +
            i['question'], "\n\n" + true_question,
            f"\n{variant_letters_check[int(questions[2][0])]}) " + questions[2][1:])


def command_one_run_game():
    user_all_variants = ""
    """"""
    player_name = input("O'yinchini ismini kiriting: ")
    user_played, true_answer_count, question_num, count_help, user_answer = 1, 0, 1, 0, ""

    try:
        with open("users.json") as file:
            users = json.load(file)
            for i in users:  # o'yinchi oldin o'ynagan bo'lsa data dan oladi
                if player_name in i.values():
                    user_played = list(i.values())[1]
                    break
        print("O'yinlar soni:", user_played)
    except:
        pass

    try:
        with open("word_test.json") as f:  # test.json ni ochiladi va foydalanuvchi bilan ishlaydi
            datas = json.load(f)

            for i in datas:  # test.json faylining har bir testiga kirish uchun sikl
                print(f"\033[36msavol {question_num}/{len(datas)}\033[0m")
                print(i['question'], "\n")
                for j in range(4):  # testning variantlarini ko'rsatish uchun sikl
                    print(variant_letters[j] + i['answers'][j]['key'])
                print("h - yordam")

                user_answer = input("Javobni kiriting: ")
                user_all_variants += user_answer

                if user_answer == "h":
                    count_help += 1
                    result = help_(question_num=question_num, i=i, count_help=count_help)
                    if result == "stop":  # yordam soni 1 dan ko'p bo'lsa qayta savol beradi
                        for j in range(4):
                            print(variant_letters[j] + i['answers'][j]['key'])
                    print("h - yordam")
                    user_answer = input("Javobni kiriting: ")
                    user_all_variants += user_answer

                while user_all_variants[-2:].count('hh') > 0 and user_answer == 'h':
                    print("\033[33mYordamdan ketma-ket 2 marta foydalanib bo'lmaydi!\033[0m")
                    help_(question_num=question_num, i=i, count_help=count_help)
                    user_answer = input("Javobni kiriting: ")

                while user_answer != "a" and user_answer != "b" and user_answer != "c" and user_answer != "d":
                    print(
                        "\033[31mXato variant kiritdingiz!\033[0m\n" + f"\033[36msavol {question_num}/{len(datas)}\033[0m\n" +
                        i['question'], "\n")
                    for j in range(4):  # testning variantlarini ko'rsatish uchun sikl
                        print(variant_letters[j] + i['answers'][j]['key'])
                    print("h - yordam")
                    user_answer = input("Javobni kiriting: ")
                    user_all_variants += user_answer

                # asosiy sikl ni to'xtashish uchun
                break_loop = ""
                # foydalanuvchi bergan javobni tekshirish uchun sikl
                for k in range(4):
                    # user bergan javob variant kaliti bo'lsa ishlaydi
                    if user_answer == variant_letters_check[k]:
                        # agar user bergan javob, bazadagi testning to'gri javobi bo'lsa ishlaydi
                        if i['answers'][k]['isTrue'] == True:
                            true_answer_count += 1
                            print("\033[32mJavob to'g'ri\033[0m")
                            win_user(question_num, player_name, user_played, true_answer_count)
                        else:
                            print(
                                "\033[31mNoto'g'ri javob\033[0m\n" + f"Ishtirokchi {player_name}\n O'yin tugadi, sizning ochkolaringiz: {true_answer_count}")
                            if is_user_have(player_name) == True:  # agar bazada user bor bo'lsa ishlaydi
                                update_user_data(name=player_name, played=user_played + 1, best_score=true_answer_count)
                            else:
                                add_user_data(name=player_name, played=user_played, best_score=true_answer_count)
                            break_loop = "break"
                            break

                if break_loop == "break":
                    break

                question_num += 1
    except:
        print("Bazada test yo'q!")


def users_rating():
    column = """---------+--------+-----------
name     | played | best_score
---------+--------+-----------"""
    try:
        with open("users.json") as f:
            data = json.load(f)
            for i in data:
                len_name, len_p, len_b = len(i['name']), len(str(i['played'])), len(str(i["best_score"]))
                column += f"""\n{i['name']}{" " * (9 - len_name)}| {i['played']}{" " * (7 - len_p)}| {i["best_score"]}{" " * (10 - len_b)}
---------+--------+-----------"""
            print(column)
    except:
        print("Hozirda reytinglar jadvali bo'sh!")


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
