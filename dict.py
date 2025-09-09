data = {
    "name": "Kwanzaa",
    "age": 20,
    "address": "Isekai"
}

data["name"] = "Arsal Fahrulloh" #ubah data array key name
data["compay"] = "PT IT" #menambhakan data array key "compay" dan isi arraykey "PT IT"
del data["address"] #menghapus data array key "address"

for key, value in data.items(): #data.item() listnya jadi tuple
    print(f"Array Key: {key}, Isi Value {value}")
    # Array Key: name, Isi Value Kwanzaa
    # Array Key: age, Isi Value 20
    # Array Key: address, Isi Value Isekai
    
    
# print(data.items()) # isinya jadi data tuple dict_items([('name', 'Kwanzaa'), ('age', 20), ('address', 'Isekai')])
# data = {
#     "name": "Kwanzaa",
#     "age": 20,
#     "address": "Isekai"
# }

# for key in data:
#     value = data[key]
#     print(f"Array Key: {key}, Isi Value {value}")
#     # Array Key: name, Isi Value Kwanzaa
#     # Array Key: age, Isi Value 20
#     # Array Key: address, Isi Value Isekai
    
# print(data.items()) # isinya jadi data tuple dict_items([('name', 'Kwanzaa'), ('age', 20), ('address', 'Isekai')])




#data tambahan
name = ("Arsal", "Kwanzza")

key, value = name
print(key)
print(value)


alamat = (("Isekai", "Bandung"), ("Jakarta", "Bali"))
almt1, almt2 = alamat
print(almt1)
print(almt2)

dtlalmt1, dtlalmt2 = almt1
print(dtlalmt1)
print(dtlalmt2)

#hasilnya
# Arsal
# Kwanzza
# ('Isekai', 'Bandung')
# ('Jakarta', 'Bali')
# Isekai
# Bandung
