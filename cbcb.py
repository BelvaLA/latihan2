"""
Created on wednesday 21 sept 2022
@author : Belva Luthfiah Andini
@author NIM : 065002200035

This code is for Tugas 2 Latihan Praktikum Algo
"""
#code ini untuk menanyakan uname 
intro = input("Hi user selamat datang diprogram kami, siapa namamu? ")
print(f"Hi {intro}, Program ini dibuat untuk membantu anda menentukan luas ruangan anda") 

#code ini menginput nilai / data yang user berikan
P = int(input("Silahkan masukan panjang ruangan: "))
L = int(input("Silahkan masukan Lebar ruangan: "))
Satuan = input("Masukan satuan yang diinginkan Meter/Inch: ")
Luas = P * L 

#code ini memberikan output dari hasil nilai / data yg user berikan
print(f"Hasil dari luas ruangan anda adalah {Luas} {Satuan} ")
