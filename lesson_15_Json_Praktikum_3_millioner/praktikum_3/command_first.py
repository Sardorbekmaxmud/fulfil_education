import json
from data_add_update import (is_user_have,
                             add_user_data,
                             update_user_data,
                             win_user, )
from help import help_

variant_letters = ["a) ", "b) ", "c) ", "d) "]
variant_letters_check = ["a", "b", "c", "d"]


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
        with open("tests.json") as f:  # test.json ni ochiladi va foydalanuvchi bilan ishlaydi
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
