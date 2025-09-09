def penjumlahan(*list_angka): # (*)untuk menandahakn parameter tipe data list
    total = 0
    angka_test = 5
    for angka in list_angka:
        total = total + angka
    return (total, angka_test, list_angka) #return nilai data tuple
    
total, data_test, data_list = penjumlahan(10,20,10,30) #variabel ini akan di simpan datanya dari return tuple
print(total)

print(f"Hasil Total: {total}, Hasil List: {data_list}, Hasil Test: {data_test}")
# Hasil Total: 70, Hasil List: (10, 20, 10, 30), Hasil Test: 5

# total = penjumlahan(10,20,10,30)
# print(total)
# hasilnya (70, 5, (10, 20, 10, 30))