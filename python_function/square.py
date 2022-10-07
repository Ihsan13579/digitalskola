#user defined function
#just take 1 parameters
# def square ():
#     """
#     Pangkat 2 operations
#     """
#     new_value = 4 ** 2
#     print(new_value)

# square()
#------------------------------------------------
# def square (value):
#     """
#     Pangkat 2 operations
#     """
#     new_value = value ** 2
#     print(new_value)

# square(5)
#-------------------------------------------------
# def square (value):
#     """
#     Pangkat 2 operations
#     """
#     new_value = value ** 2
#     # print(new_value)
#     return new_value

# hasil=square(10)
# print(hasil)

#----------------------------------------------------
#take 2 parameters function
# def perkalian(angka1, angka2):
#     """_summary_
#     Fungsi yang berguna untuk perkalian
#     Args:
#         angka1 (_type_): Integer
#             _description_
#         angka2 (_type_): Integer
#             _description_

#     Returns: Integer
#         _type_: Hasil Perkalian
#     """
#     new_value = angka1 * angka2
#     return new_value
# hasil = perkalian(2,2)
# print(type(hasil))
# print(hasil)

#--------------------------------------------------
#return multiple values
# def return_multiple(angka1:int, angka2:int):
#     """
#     Fungsi yang mengembalikan 2 values
#     """
#     perkalian = angka1*angka2
#     penambahan=angka1+angka2

#     multiple_value = [perkalian, penambahan]
#     return multiple_value
# hasil = return_multiple(3,3)
# print(hasil)
# print(hasil[0])
# print(hasil[1])
#--------------------------------------------------
#return multiple values
def return_multiple(angka1:int, angka2:int):
    """
    Fungsi yang mengembalikan 2 values
    """
    perkalian = angka1*angka2
    penambahan=angka1+angka2

    # multiple_value = [perkalian, penambahan]
    return perkalian, penambahan
x,y = return_multiple(3,3)
print(x), print(y)
