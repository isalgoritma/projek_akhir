import os
from tabulate import tabulate

# Fungsi Clear Screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Fungsi Input Wajib
def input_wajib(prompt):
    while True:
        data = input(prompt)
        if data.strip() == "":
            print("Input wajib diisi!")
        else:
            return data

# Data akun & aktivitas
akun = {}
aktivitas = [
    {'nama': 'Mewarnai', 'kategori': 'Sensorik', 'durasi': 20, 'manfaat': 8},
    {'nama': 'Puzzle', 'kategori': 'Motorik', 'durasi': 15, 'manfaat': 7},
    {'nama': 'Membuat Kolase', 'kategori': 'Sensorik', 'durasi': 20, 'manfaat': 6},
    {'nama': 'Pasir Kinetik', 'kategori': 'Sensorik', 'durasi': 15, 'manfaat': 9},
    {'nama': 'Bola Kecil', 'kategori': 'Motorik', 'durasi': 10, 'manfaat': 7},
    {'nama': 'Storytelling', 'kategori': 'Komunikasi', 'durasi': 15, 'manfaat': 8},
    {'nama': 'Musik Sederhana', 'kategori': 'Sensorik', 'durasi': 15, 'manfaat': 7},
    {'nama': 'Menyusun Balok', 'kategori': 'Motorik', 'durasi': 20, 'manfaat': 6},
    {'nama': 'Bermain Peran', 'kategori': 'Sosial', 'durasi': 20, 'manfaat': 8},
    {'nama': 'Yoga Anak', 'kategori': 'Sensorik', 'durasi': 15, 'manfaat': 7},
]

# Estimasi durasi fokus
def estimasi_durasi(umur):
    if 3 <= umur <= 5:
        return (5, 60)
    elif 6 <= umur <= 8:
        return (10, 90)
    elif 9 <= umur <= 12:
        return (15, 120)
    else:
        return (10, 90)

# Fungsi Register
def register():
    while True:
        clear_screen()
        print("=== Registrasi Akun ===")
        nama = input_wajib("Nama (huruf): ")
        if not nama.replace(" ", "").isalpha():
            print("Nama hanya huruf!")
            continue
        username = input_wajib("Username: ")
        if username in akun:
            print("Username sudah dipakai!")
            continue
        no_telp = input_wajib("No. Telepon (angka): ")
        if not no_telp.isdigit():
            print("Telepon hanya angka!")
            continue
        password = input_wajib("Password: ")
        akun[username] = {'nama': nama, 'telepon': no_telp, 'password': password}
        break
    clear_screen()

# Fungsi Login
def login():
    clear_screen()
    print("=== Login Akun ===")
    username = input_wajib("Username: ")
    password = input_wajib("Password: ")
    if username in akun and akun[username]['password'] == password:
        clear_screen()
        return True
    else:
        print("Login gagal.")
        return False

# Binary Search Aktivitas by Nama
def binary_search(data, key):
    data.sort(key=lambda x: x['nama'])
    kiri, kanan = 0, len(data)-1
    while kiri <= kanan:
        mid = (kiri + kanan) // 2
        if data[mid]['nama'] == key:
            return data[mid]
        elif data[mid]['nama'] < key:
            kiri = mid+1
        else:
            kanan = mid-1
    return None

# Program Utama
while True:
    clear_screen()
    print("=== Aplikasi Rekomendasi Aktivitas Anak Autisme ===")
    print("1. Register\n2. Login\n3. Keluar")
    menu = input_wajib("Pilih menu: ")

    if menu == '1':
        register()

    elif menu == '2':
        if login():
            # Input profil anak
            while True:
                clear_screen()
                nama_anak = input_wajib("Nama Anak: ")
                if not nama_anak.replace(" ", "").isalpha():
                    print("Nama hanya huruf!")
                    continue
                try:
                    umur_anak = int(input_wajib("Umur Anak: "))
                    durasi_maks, total_harian_maks = estimasi_durasi(umur_anak)
                    print(f"\nEstimasi maksimal per aktivitas: {durasi_maks} menit")
                    print(f"Total waktu edukasi harian maksimal: {total_harian_maks} menit\n")
                    input("Tekan Enter untuk lanjut...")
                    break
                except ValueError:
                    print("Umur harus angka!")

            durasi_maks, total_harian_maks = estimasi_durasi(umur_anak)
            while True:
                try:
                    total_waktu = int(input_wajib("Total waktu edukasi (menit): "))
                    if total_waktu > total_harian_maks:
                        print(f"Terlalu lama! Maks: {total_harian_maks} menit")
                    else:
                        break
                except ValueError:
                    print("Harus angka!")

            # Input preferensi
            pref = ['Sensorik','Motorik','Sosial','Komunikasi','Semua']
            while True:
                print("Preferensi (Sensorik/Motorik/Sosial/Komunikasi/Semua)")
                preferensi = input_wajib("Pilih: ").capitalize()
                if preferensi in pref:
                    break
                print("Pilihan tidak valid!")

            # Input waktu edukasi
            while True:
                try:
                    total_waktu = int(input_wajib("Total waktu edukasi (menit): "))
                    if total_waktu > 3*durasi_maks:
                        print(f"Terlalu lama! Maks: {3*durasi_maks} menit")
                    else:
                        break
                except ValueError:
                    print("Harus angka!")

            # Filter aktivitas & hitung rasio
            if preferensi != 'Semua':
                aktivitas_pilihan = [a for a in aktivitas if a['kategori'] == preferensi]
            else:
                aktivitas_pilihan = aktivitas.copy()
            for a in aktivitas_pilihan:
                a['rasio'] = a['manfaat'] / a['durasi']

            aktivitas_pilihan.sort(key=lambda x: x['rasio'], reverse=True)

            # Greedy Knapsack
            rekomendasi, waktu_tersisa, total_manfaat = [], total_waktu, 0
            for a in aktivitas_pilihan:
                if a['durasi'] <= waktu_tersisa:
                    rekomendasi.append(a)
                    waktu_tersisa -= a['durasi']
                    total_manfaat += a['manfaat']

            clear_screen()
            print(f"Rekomendasi untuk {nama_anak} ({umur_anak} th)\n")
            headers = ['Aktivitas','Kategori','Durasi','Manfaat']
            tabel = [[r['nama'], r['kategori'], r['durasi'], r['manfaat']] for r in rekomendasi]
            print(tabulate(tabel, headers=headers, tablefmt="fancy_grid"))
            print(f"\nTotal Manfaat: {total_manfaat}")
            print(f"Sisa Waktu: {waktu_tersisa} menit")

            input("\nTekan Enter untuk kembali ke menu utama...")
        else:
            input("Login gagal. Enter untuk lanjut...")

    elif menu == '3':
        clear_screen()
        print("Terima kasih.")
        break

    else:
        print("Menu tidak tersedia.")
