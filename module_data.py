def sayHello(inputText):
    print(f"Anda Mengetik: {inputText}")
    
class Test:
    no = 10
    def __init__(self, angka_pertama, angka_kedua):
        self.angka1 = angka_pertama
        self.angka2 = angka_kedua
        self.penjumlahan()
        
    def penjumlahan(self):
        total_jumlah = self.angka1 + self.angka2
        print(f"Hasil Penjmlahan {self.angka1} + {self.angka2} = {total_jumlah}")
        
    def perkalian(self):
        total_perkalian = self.angka1 * self.angka2 * self.no
        return f"Hasil dari {self.angka1} * {self.angka2} * {self.no} = {total_perkalian}"