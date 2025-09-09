input_data = int(input("Masukkan berapa Banyak?"))

umur = []
nama = []

for no in range(0, input_data):
    print(f"Ini input ke-{no}")
    input_nama = input("Masukkan Nama: ")
    input_umur = input("Masukkan Umur: ")
    
    nama.append(input_nama)
    umur.append(input_umur)
    
for no in range(0, len(nama)): #len adalah meghitung panjang list
    data_nama = nama[no] #data_nama menyimpan isi list dari nama dan index dari perulangan no
    data_umur = umur[no]
    print(f"Nama: {data_nama}, Umur: {data_umur}")