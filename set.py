# set untuk menyimpan data unique| tidk akan duplikat

#set => {}
#list => []
#tuple => ()

nama = {"Kwanzaa","Arsal","Kwanzaa","Arsal","Fahrulloh"}
nama.add("Test") #untuk menambahkan data dlm set
nama.remove("Arsal") #untuk menghapus data dlm list
print(nama) #hasilnya {'Kwanzaa', 'Arsal', 'Fahrulloh'} |{'Fahrulloh', 'Kwanzaa', 'Arsal'} hasilnya random
# print(nama[0]) set tidak bisa diambil indexnya karena hasilnya random