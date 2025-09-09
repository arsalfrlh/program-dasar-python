nama = ["Kwanzaa","Arsal","Fahrulloh"] # ini list
nama.append("Test") #append untuk menambhakan Test kdlm list dan di sinpan di index terakhir

print(nama)

print(nama[0]) #menampilkan nama sesuai index (Kwanzza)
print(nama[1])
print(nama[2])
print(nama[3])

print(len(nama)) # menampilkan jumlah data dlm list| bukan index hasilnya (3)| hasilnya (4)

nama.remove("Fahrulloh") #menghapus nama dlm list
print(nama)

nama[2] = "Sasa" #memilih index 2 (Test) dan di ganti jadi Sasa
print(nama)