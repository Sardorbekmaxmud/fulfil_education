from lesson_12_F18_polimorfizm_paket_modul.paket3 import add_numbers, sub_numbers, mul_numbers, div_numbers

i = int(input("i: "))
j = int(input("j: "))

x1 = div_numbers(mul_numbers(add_numbers(i, j), add_numbers(j, 45)), sub_numbers(10, i))
x2 = ((i + j) * (j + 45)) / (10 - i)

print(x1)
print(x2)
