#perulangan while akan terus di exsekusi jika nilainya true, dan akan berhenti jika nilainya false
data = ""

while data != 'quit':
    print("Masukkan Kata, Ketik quit untuk keluar")
    data = input()
    print(f"Anda Mengetik: {data}")
    print("\n")