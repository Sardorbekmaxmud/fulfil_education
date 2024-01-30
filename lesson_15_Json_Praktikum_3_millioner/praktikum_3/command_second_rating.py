import json


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
