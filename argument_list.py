def penjumlahan(x, *list_angka): # (*)untuk menandahakn parameter tipe data list
    total = 0
    for angka in list_angka:
        total = total + angka + x
    print(f"Total List {list_angka} + Total {x} = {total}")
    print(x)
    
penjumlahan(100,20,10,30) #parameter x (100)| parameter list_angka (20,10,30)