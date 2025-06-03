import os
from tabulate import tabulate 
import pyfiglet
from colorama import Fore, Style

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

def input_profil():
    clear_screen()
    print("==== INPUT PROFIL ANAK ====")
    
    while True:
        nama_anak = inputan_wajib("Nama anak: ")
        if nama_anak.replace(" ", "").isalpha():
            break
        else:
            print("Nama berupa huruf!")
    
    while True:
        try:
            umur = int(inputan_wajib("Umur anak (tahun): "))
            if 1 <= umur <= 12:
                break
            else:
                print("Umur harus antara 1-12 tahun!")
        except ValueError:
            print("Umur harus berupa angka!")
    
    print("\nKategori aktivitas yang tersedia:")
    print("1. Sensorik")
    print("2. Motorik") 
    print("3. Komunikasi")
    print("4. Sosial")
    
    while True:
        try:
            kategori_pilihan = int(inputan_wajib("Pilih kategori favorit (1-4): "))
            if 1 <= kategori_pilihan <= 4:
                kategori_map = {1: 'Sensorik', 2: 'Motorik', 3: 'Komunikasi', 4: 'Sosial'}
                kategori_favorit = kategori_map[kategori_pilihan]
                break
            else:
                print("Pilihan harus antara 1-4!")
        except ValueError:
            print("Pilihan harus berupa angka!")
    
    return {
        'nama_anak': nama_anak,
        'umur': umur,
        'kategori_favorit': kategori_favorit
    }

def input_waktu():
    clear_screen()
    print("==== INPUT WAKTU TERSEDIA ====")
    
    while True:
        try:
            waktu_tersedia = int(inputan_wajib("Waktu yang tersedia (menit): "))
            if waktu_tersedia > 0:
                break
            else:
                print("Waktu harus lebih dari 0 menit!")
        except ValueError:
            print("Waktu harus berupa angka!")
    
    return waktu_tersedia

def hitung_fokus_preferensi(profil_anak, waktu_tersedia):
   
    aktivitas_sesuai = [act for act in aktivitas if act['kategori'] == profil_anak['kategori_favorit']]
    
    aktivitas_waktu = [act for act in aktivitas_sesuai if act['durasi'] <= waktu_tersedia]
    
    if not aktivitas_waktu:
        aktivitas_waktu = [act for act in aktivitas if act['durasi'] <= waktu_tersedia]
    
    aktivitas_terurut = sorted(aktivitas_waktu, key=lambda x: (-x['manfaat'], x['durasi']))
    
    return aktivitas_terurut

def tampilkan_rekomendasi(profil_anak, rekomendasi):
    clear_screen()
    print(f"==== REKOMENDASI AKTIVITAS UNTUK {profil_anak['nama_anak'].upper()} ====")
    print(f"Umur: {profil_anak['umur']} tahun")
    print(f"Kategori Favorit: {profil_anak['kategori_favorit']}")
    print()
    
    if not rekomendasi:
        print("Maaf, tidak ada aktivitas yang sesuai dengan waktu tersedia.")
        print("Coba tambah waktu atau pilih kategori lain.")
    else:
       
        top_rekomendasi = rekomendasi[:5]
        
        headers = ["No", "Nama Aktivitas", "Kategori", "Durasi (menit)", "Skor Manfaat"]
        table_data = []
        
        for i, act in enumerate(top_rekomendasi, 1):
            table_data.append([
                i,
                act['nama'],
                act['kategori'],
                act['durasi'],
                act['manfaat']
            ])
        
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        
        print(f"\n{Fore.GREEN}✓ Aktivitas teratas: {top_rekomendasi[0]['nama']}{Style.RESET_ALL}")
        print(f"Durasi: {top_rekomendasi[0]['durasi']} menit | Skor: {top_rekomendasi[0]['manfaat']}/10")

def menu_akhir():
    while True:
        print("\n==== MENU AKHIR ====")
        print("1. Kembali ke Menu Utama")
        print("2. Keluar Program")
        
        try:
            pilihan = int(inputan_wajib("Pilih opsi (1-2): "))
            if pilihan == 1:
                return False 
            elif pilihan == 2:
                print("Terima kasih telah menggunakan EDJUST!")
                return True   
            else:
                print("Pilihan harus 1 atau 2!")
        except ValueError:
            print("Pilihan harus berupa angka!")

def menu_utama():
    while True:
        clear_screen()
        judul = pyfiglet.figlet_format("EDJUST", font = "big")
        print(Fore.BLUE + judul + Style.RESET_ALL)
        print("==== MENU UTAMA ====")
        print("1. Registrasi Akun")
        print("2. Login")
        print("3. Keluar")
        
        try:
            pilihan = int(inputan_wajib("Pilih menu (1-3): "))
            
            if pilihan == 1:
                registrasi()
                input("Tekan Enter untuk melanjutkan...")
                
            elif pilihan == 2:
                if login():
                    while True:
                        clear_screen()
                        print("==== DASHBOARD EDJUST ====")
                        print("1. Mulai Rekomendasi Aktivitas")
                        print("2. Logout")
                        
                        try:
                            sub_pilihan = int(inputan_wajib("Pilih menu (1-2): "))
                            
                            if sub_pilihan == 1:
                                profil = input_profil()
                                waktu = input_waktu()
                                rekomendasi = hitung_fokus_preferensi(profil, waktu)
                                tampilkan_rekomendasi(profil, rekomendasi)
                                
                                if menu_akhir():
                                    return 
                                else:
                                    continue  
                                    
                            elif sub_pilihan == 2:
                                print("Logout berhasil!")
                                break
                            else:
                                print("Pilihan harus 1 atau 2!")
                                input("Tekan Enter untuk melanjutkan...")
                        except ValueError:
                            print("Pilihan harus berupa angka!")
                            input("Tekan Enter untuk melanjutkan...")
                            
            elif pilihan == 3:
                print("Terima kasih telah menggunakan EDJUST!")
                break
            else:
                print("Pilihan harus antara 1-3!")
                input("Tekan Enter untuk melanjutkan...")
        except ValueError:
            print("Pilihan harus berupa angka!")
            input("Tekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    menu_utama()






