import os
from tabulate import tabulate 
import pyfiglet
from colorama import Fore, Style
# import pandas as pd

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def inputan_wajib(prompt):
    while True:
        data = input(prompt)
        if data.strip() == "":
            print("Wajib diisi!")
        else:
            return data

akun_data = {}

aktivitas = [
    {'nama': 'Mewarnai', 'kategori': 'Sensorik', 'durasi': 20, 'manfaat': 8},
    {'nama': 'Puzzle', 'kategori': 'Motorik', 'durasi': 15, 'manfaat': 7},
    {'nama': 'Membuat Kolase', 'kategori': 'Sensorik', 'durasi': 20, 'manfaat': 6},
    {'nama': 'Bermain Pasir Kinetik', 'kategori': 'Sensorik', 'durasi': 15, 'manfaat': 9},
    {'nama': 'Bermain Bola Kecil', 'kategori': 'Motorik', 'durasi': 10, 'manfaat': 7},
    {'nama': 'Storytelling Bergambar', 'kategori': 'Komunikasi', 'durasi': 15, 'manfaat': 8},
    {'nama': 'Bermain Musik Sederhana', 'kategori': 'Sensorik', 'durasi': 15, 'manfaat': 7},
    {'nama': 'Menyusun Balok', 'kategori': 'Motorik', 'durasi': 20, 'manfaat': 6},
    {'nama': 'Bermain Peran', 'kategori': 'Sosial', 'durasi': 20, 'manfaat': 8},
    {'nama': 'Yoga Anak', 'kategori': 'Sensorik', 'durasi': 15, 'manfaat': 7},
]

clear_screen()
judul = pyfiglet.figlet_format("EDJUST", font = "big")
print(Fore.BLUE + judul + Style.RESET_ALL)
        

def registrasi():
    while True:
        clear_screen()
        print("==== REGISTRASI AKUN ====")
        
        while True:
            nama = inputan_wajib("Nama: ")
            if nama.replace(" ", "").isalpha():
                break
            else:
                print("Nama berupa huruf!")

        while True:
            no_hp = inputan_wajib("No. telepon: ")
            if no_hp.isdigit():
                break
            else:
                print("No. telepon hanya berupa angka!")
        
        while True:
            username = inputan_wajib("Username: ")
            if username in akun_data:
                print("Username sudah digunakan.")
                print("Silahkan coba lagi!")
            else:
                break
        
        password = inputan_wajib("Password: ")
            
        akun_data[username] = {'nama' : nama, 'telepon' : no_hp, 'password' : password}
        print("Registrasi berhasil!")
        break

    clear_screen()

def login():
    while True:
        clear_screen()
        print("==== LOGIN AKUN ====")

        username = inputan_wajib("Username: ")
        if username not in akun_data:
            print("Username tidak ditemukan. Coba lagi!")
            continue
        
        while True:
            password = inputan_wajib("Password: ")
            if akun_data[username]['password'] == password:
                print("Login berhasil!")
                clear_screen()
                return True
            else:
                print("Login gagal.Silahkan coba lagi!")
    clear_screen()






