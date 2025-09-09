import module_data
from module_data import Test

input_user = input("Masukkan Teks: ")
module_data.sayHello(input_user)
# model_data.sayHello(inputText=input_user)

input_angka1 = int(input("Masukkan Angka Pertama: "))
input_angka2 = int(input("Masukkan Angka Kedua: "))

test = module_data.Test(input_angka1, input_angka2)
perkalian = test.perkalian()
print(perkalian)