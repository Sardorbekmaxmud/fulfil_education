import json


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
    with open("tests.json") as f:
        datas = json.load(f)
    if question_num == len(datas):
        if is_user_have(player_name) == True:
            update_user_data(name=player_name, played=user_played + 1, best_score=true_answer_count)
        else:
            add_user_data(name=player_name, played=user_played, best_score=true_answer_count)