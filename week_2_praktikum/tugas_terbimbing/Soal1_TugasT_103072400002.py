import numpy as np

# data
nama = []
nim = []
nilai = []
tahun = []

while True:
    # menu
    print("\n Menu Mahasiswa")
    print("1. Input Mahasiswa")
    print("2. Delete Mahasiswa")
    print("3. Search Mahasiswa")
    print("4. Keluar")

    pilih = input("Pilih menu: ")

    # input
    if pilih == "1":
        n = input("Nama: ")
        ni = input("NIM: ")
        nl = float(input("Nilai: "))
        th = int(input("Tahun masuk: "))

        nama.append(n)
        nim.append(ni)
        nilai.append(nl)
        tahun.append(th)

        print("Data berhasil ditambahkan")

    # delete
    elif pilih == "2":
        cari = input("Masukkan nama atau NIM yang ingin dihapus: ")

        nama_np = np.array(nama)
        nim_np = np.array(nim)

        # find
        idx = np.where((nama_np == cari) | (nim_np == cari))[0]

        if len(idx) > 0:
            i = idx[0]

            # remove
            nama.pop(i)
            nim.pop(i)
            nilai.pop(i)
            tahun.pop(i)

            print("Data berhasil dihapus")
        else:
            print("Data tidak ditemukan")

    # search
    elif pilih == "3":
        cari = input("Masukkan nama atau NIM: ")

        nama_np = np.array(nama)
        nim_np = np.array(nim)

        # find
        idx = np.where((nama_np == cari) | (nim_np == cari))[0]

        if len(idx) > 0:
            i = idx[0]

            print("\nData ditemukan")
            print("Nama:", nama[i])
            print("NIM:", nim[i])
            print("Nilai:", nilai[i])
            print("Tahun masuk:", tahun[i])
        else:
            print("Data tidak ditemukan")

    # exit
    elif pilih == "4":
        print("Program selesai")
        break

    # error
    else:
        print("Menu tidak valid")

# Program dimulai dengan menyiapkan tempat penyimpanan data mahasiswa (nama, nim, nilai, tahun)

# Program masuk ke loop menu agar user bisa menjalankan fitur berulang kali

# User memilih menu dari CLI

# Jika memilih input:
# Data mahasiswa dimasukkan oleh user lalu disimpan ke dalam list

# Jika memilih delete:
# Program mencari mahasiswa berdasarkan nama atau NIM
# Jika ditemukan, data mahasiswa dihapus dari penyimpanan

# Jika memilih search:
# Program mencari mahasiswa di data yang tersimpan
# Jika ditemukan, detail data mahasiswa ditampilkan

# Jika memilih keluar:
# Program menghentikan loop dan selesai
