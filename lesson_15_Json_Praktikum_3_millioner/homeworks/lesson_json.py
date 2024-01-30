import json

# import googlemaps
# import requests

# wiki = "https://en.wikipedia.org/wiki/JSON"
# response = requests.get(wiki)

# print(json.dumps(response.json(), indent=4, sort_keys=True))


# data = {"Model": "Malibu", "Rang": "Qora", "Yil": 2020, "Narh": 40000}
#
# # print(json.dumps(data))
#
# talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""

# talaba = json.loads(talaba_json)
# print(talaba['ism'], talaba['familiya'])

# with open("data.json", 'w') as f:
#     json.dump(data, f, indent=4)
#
# with open("talaba.json", 'w') as f:
#     json.dump(talaba, f, indent=4)

# with open("students.json") as f:
#     students = json.load(f)
#
# for i in students['student']:
#     print(f"{i['name']} {i['lastname']}, {i['year']}-kurs, {i['faculty']} talabasi")

# with open("api-result.json") as f:
#     python = json.load(f)

# print(python['query']['pages']['13801']['title'])
# print(python['query']['pages']['13801']['extract'])
# extract = [print(i+".") for i in python['query']['pages']['13801']['extract'].split(". ")]
# print(extract)


# data = {
#     "name": "Sardorbek",
#     "age": 21,
#     "family": {
#         "father": {
#             "name": "Xolmo'min",
#             "age": "48",
#         },
#         "mother": {
#             "name": "Yulduz",
#             "age": "44",
#         },
#         "brother": {
#             "name": "Sanjarbek",
#             "age": "18",
#         },
#         "sister": {
#             "name": "Shabnam",
#             "age": "11",
#         }
#     },
#     "hobby": ["futboll", "walk", "ciycling"],
#     "my_reading_books": ("14 yoshli kapitan", "Tarixi Muhammadiy", "Iymon"),
#     "isstudying": True,
#     "isEating": False
# }

# json_data = json.dumps(data, indent=4)
# print(json_data)
#
# data_ = json.loads(json_data)
# print(data_["family"])


# class_int = 5
# class_float = 5.0
# class_str = "string"
# class_bool_true = True
# class_bool_false = False
# class_none = None
# class_dict = {"type": "clothe", "size": 46}
# class_list = [1, 2, 4, 5, 7]
# class_tuple = ("t", "g", "h", "s", "a", "d")
#
# json_int = json.dumps(class_int)
# json_float = json.dumps(class_float)
# json_string = json.dumps(class_str)
# json_true = json.dumps(class_bool_true)
# json_false = json.dumps(class_bool_false)
# json_null = json.dumps(class_none)
# json_object_or_str = json.dumps(class_dict)
# json_array = json.dumps(class_list)
# json_array_2 = json.dumps(class_tuple)
#
# print(json_int, type(json_int))
# print(json_float, type(json_float))
# print(json_string, type(json_string))
# print(json_true, type(json_true))
# print(json_false, type(json_false))
# print(json_null, type(json_null))
# print(json_object_or_str, type(json_object_or_str))
# print(json_array, type(json_array))
# print(json_array_2, type(json_array_2))


# import os
# os.remove("for_test.txt")
# os.remove("for_test2.txt")
#
# with open("students.json", "a") as f:
#     json.dump(api, f, indent=4)
# file.close()
# file.write("gdgdrt")


# --------------------TRY EXCEPT-----------------------------------------------------
# import json
# import requests
#
# responce = requests.get('https://jsonplaceholder.typicode.com/todos')
# todos = json.loads(responce.text)
# if todos == responce.json():
#     print(True)
# print(type(todos))
# print(todos[:10])
#
# # with open("site_json_data.json", "w") as site_json:
# #     site_json.write(responce.text)


# with open("myfile.docx", 'r') as f:
# print(f.write("fasfda"))
# with open("my_file.json", "w") as f:
#
#     json.dump({"asdfas": "a"}, f, indent=4)



