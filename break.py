for no in range(0, 101):
    if(no == 50):
        break
    print(no)
    
    
while True:
    input_user = input("Ketik quit untuk keluar, Masukkan Kata: ")
    if(input_user == "quit"):
        print("Anda telah keluar")
        break
    print(f"Anda Mengetikkan: {input_user}")