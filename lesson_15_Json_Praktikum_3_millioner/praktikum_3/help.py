variant_letters = ["a) ", "b) ", "c) ", "d) "]
variant_letters_check = ["a", "b", "c", "d"]


def help_(question_num, i, count_help):
    """Yordam funksiyasi"""
    if count_help > 1:
        print(" Siz yordamdan foydalanib bo'ldingiz.\n" + f"\033[36msavol {question_num}/10\033[0m\n" + i[
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
            f"  {(questions[0][1:])} va {questions[1][1:]} variantlari olib tashlandi\n" + f"\033[36msavol {question_num}/10\033[0m\n" +
            i['question'], "\n\n" + true_question,
            f"\n{variant_letters_check[int(questions[2][0])]}) " + questions[2][1:])