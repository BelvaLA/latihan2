intro = input("Hi user, siapa namamu? ")
print(f"Hi {intro}, Program ini dibuat untuk membantu anda menentukan luas ruangan anda")

P = int(input("Silahkan masukan panjang ruangan: "))
L = int(input("Silahkan masukan Lebar ruangan: "))
Satuan = input("Masukan satuan yang diinginkan Meter/Inci: ")
Jumlah = P * L

print(f"Hasil dari luas ruangan anda adalah {Jumlah} {Satuan} ")