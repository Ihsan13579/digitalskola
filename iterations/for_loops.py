# numbers = [6,5,7,4,9,7,9]

# sum=0

# for num in numbers:
#     sum = sum + num
#     print(sum)

# print(f'totalnya adalah {sum}')

#dict {key:value}
dict_1 = {"name": "angga", "umur": 29, "pekerjaan": "ekspor-impor"}

for key in dict_1.keys():
    print(key)

for value in dict_1.values():
    print(value)

for key, value in dict_1.items():
    print(key, " = ", value)