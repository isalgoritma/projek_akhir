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
    estimasi = hitung_estimasi_fokus(profil_anak['umur'])
    
    aktivitas_sesuai = [act for act in aktivitas if act['kategori'] == profil_anak['kategori_favorit']]
    
    aktivitas_fokus = [act for act in aktivitas_sesuai if act['durasi'] <= estimasi['durasi_fokus_max']]
    
    if not aktivitas_fokus:
        aktivitas_fokus = [act for act in aktivitas if act['durasi'] <= estimasi['durasi_fokus_max']]
    
    aktivitas_waktu = [act for act in aktivitas_fokus if act['durasi'] <= waktu_tersedia]
    
    if not aktivitas_waktu:
        aktivitas_waktu = sorted(aktivitas, key=lambda x: x['durasi'])[:3]
    
    aktivitas_terurut = sorted(aktivitas_waktu, key=lambda x: (-x['manfaat'], x['durasi']))
    
    return aktivitas_terurut, estimasi

def tampilkan_rekomendasi(profil_anak, rekomendasi, estimasi):
    clear_screen()
    print(f"==== REKOMENDASI AKTIVITAS UNTUK {profil_anak['nama_anak'].upper()} ====")
    print(f"Umur: {profil_anak['umur']} tahun")
    print(f"Kategori Favorit: {profil_anak['kategori_favorit']}")
    print(f"Durasi Fokus Optimal: {estimasi['durasi_fokus_min']}-{estimasi['durasi_fokus_max']} menit per aktivitas")
    print()
    
    if not rekomendasi:
        print("Maaf, tidak ada aktivitas yang sesuai dengan waktu tersedia.")
        print("Coba tambah waktu atau pilih kategori lain.")
    else:
       
        top_rekomendasi = rekomendasi[:5]
        
        headers = ["No", "Nama Aktivitas", "Kategori", "Durasi (menit)", "Skor Manfaat", "Status Fokus"]
        table_data = []
        
        for i, act in enumerate(top_rekomendasi, 1):
            if act['durasi'] <= estimasi['durasi_fokus_max']:
                status_fokus = "✓ Optimal"
            else:
                status_fokus = "⚠ Perlu Jeda"
                
            table_data.append([
                i,
                act['nama'],
                act['kategori'],
                act['durasi'],
                act['manfaat'],
                status_fokus
            ])
        
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        
        print(f"\n{Fore.GREEN}✓ Aktivitas teratas: {top_rekomendasi[0]['nama']}{Style.RESET_ALL}")
        print(f"Durasi: {top_rekomendasi[0]['durasi']} menit | Skor: {top_rekomendasi[0]['manfaat']}/10")
        
        print(f"\n{Fore.CYAN}💡 Tips untuk usia {profil_anak['umur']} tahun:{Style.RESET_ALL}")
        print(f"• Berikan jeda istirahat 5-10 menit setiap {estimasi['durasi_fokus_max']} menit")
        print(f"• Total waktu edukasi harian disarankan: {estimasi['total_edukasi_min']}-{estimasi['total_edukasi_max']} menit")
        print(f"• Variasikan jenis aktivitas untuk menjaga minat anak")

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
                                waktu = input_waktu_dengan_validasi(profil)
                                rekomendasi, estimasi = hitung_fokus_preferensi(profil, waktu)
                                tampilkan_rekomendasi(profil, rekomendasi, estimasi)
                                
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

def hitung_estimasi_fokus(umur):
    if 3 <= umur <= 5:
        return {
            'durasi_fokus_min': 5,
            'durasi_fokus_max': 10,
            'total_edukasi_min': 30,
            'total_edukasi_max': 60,
            'kategori_umur': '3-5 tahun'
        }
    elif 6 <= umur <= 8:
        return {
            'durasi_fokus_min': 10,
            'durasi_fokus_max': 20,
            'total_edukasi_min': 60,
            'total_edukasi_max': 90,
            'kategori_umur': '6-8 tahun'
        }
    elif 9 <= umur <= 12:
        return {
            'durasi_fokus_min': 15,
            'durasi_fokus_max': 25,
            'total_edukasi_min': 90,
            'total_edukasi_max': 120,
            'kategori_umur': '9-12 tahun'
        }
    else:
        return {
            'durasi_fokus_min': 10,
            'durasi_fokus_max': 15,
            'total_edukasi_min': 45,
            'total_edukasi_max': 75,
            'kategori_umur': 'Umum'
        }

def tampilkan_estimasi_fokus(profil_anak):
    estimasi = hitung_estimasi_fokus(profil_anak['umur'])
    
    print(f"\n==== ESTIMASI FOKUS UNTUK {profil_anak['nama_anak'].upper()} ====")
    print(f"Kategori Umur: {estimasi['kategori_umur']}")
    print(f"Durasi Fokus Maksimal per Aktivitas: {estimasi['durasi_fokus_min']}-{estimasi['durasi_fokus_max']} menit")
    print(f"Total Waktu Edukasi Harian yang Disarankan: {estimasi['total_edukasi_min']}-{estimasi['total_edukasi_max']} menit")
    print("=" * 60)

def validasi_waktu_edukasi(waktu_input, profil_anak):
    estimasi = hitung_estimasi_fokus(profil_anak['umur'])
    
    if waktu_input <= estimasi['total_edukasi_max']:
        if waktu_input >= estimasi['total_edukasi_min']:
            return True, "optimal"
        else:
            return True, "dibawah"
    else:
        return False, "melebihi"

def input_waktu_dengan_validasi(profil_anak):
    clear_screen()
    
    tampilkan_estimasi_fokus(profil_anak)
    
    print("\n==== INPUT TOTAL WAKTU EDUKASI HARIAN ====")
    
    while True:
        try:
            waktu_tersedia = int(inputan_wajib("Total waktu edukasi yang diinginkan (menit): "))
            if waktu_tersedia > 0:
                valid, status = validasi_waktu_edukasi(waktu_tersedia, profil_anak)
                estimasi = hitung_estimasi_fokus(profil_anak['umur'])
                
                if status == "optimal":
                    print(f"{Fore.GREEN}✓ Waktu yang dipilih sangat sesuai untuk usia {profil_anak['umur']} tahun!{Style.RESET_ALL}")
                    break
                elif status == "dibawah":
                    print(f"{Fore.YELLOW}⚠ Waktu yang dipilih sedikit di bawah rekomendasi.{Style.RESET_ALL}")
                    print(f"Rekomendasi: {estimasi['total_edukasi_min']}-{estimasi['total_edukasi_max']} menit")
                    
                    konfirmasi = input("Apakah Anda ingin melanjutkan? (y/n): ").lower()
                    if konfirmasi == 'y':
                        break
                    else:
                        continue
                elif status == "melebihi":
                    print(f"{Fore.RED}⚠ PERINGATAN: Waktu yang dipilih melebihi rekomendasi untuk usia {profil_anak['umur']} tahun!{Style.RESET_ALL}")
                    print(f"Rekomendasi maksimal: {estimasi['total_edukasi_max']} menit")
                    print("Waktu belajar yang terlalu lama dapat menyebabkan anak kelelahan dan kehilangan fokus.")
                    
                    print("\nPilihan:")
                    print("1. Sesuaikan waktu dengan rekomendasi")
                    print("2. Tetap lanjutkan dengan waktu yang dipilih")
                    
                    try:
                        pilihan = int(input("Pilih opsi (1-2): "))
                        if pilihan == 1:
                            continue
                        elif pilihan == 2:
                            print(f"{Fore.YELLOW}⚠ Pastikan untuk memberikan jeda istirahat yang cukup!{Style.RESET_ALL}")
                            break
                        else:
                            print("Pilihan harus 1 atau 2!")
                            continue
                    except ValueError:
                        print("Pilihan harus berupa angka!")
                        continue
            else:
                print("Waktu harus lebih dari 0 menit!")
        except ValueError:
            print("Waktu harus berupa angka!")
    
    return waktu_tersedia

if __name__ == "__main__":
    menu_utama()






