import numpy as np

# data
nama = []
kode = []
jumlah = []
harga = []

while True:
    # menu
    print("\n MENU INVENTARIS")
    print("1. Input Barang")
    print("2. Delete Barang")
    print("3. Search Barang")
    print("4. Keluar")

    pilih = input("Pilih menu: ")

    # input
    if pilih == "1":
        nama_barang = input("Nama barang: ")
        kode_barang = input("Kode barang: ")
        jml = int(input("Jumlah: "))
        hrg = float(input("Harga per unit: "))

        nama.append(nama_barang)
        kode.append(kode_barang)
        jumlah.append(jml)
        harga.append(hrg)

        print("Barang berhasil ditambahkan")

    # delete
    elif pilih == "2":
        cari = input("Masukkan nama atau kode barang yang ingin dihapus: ")

        nama_np = np.array(nama)
        kode_np = np.array(kode)

        # search
        idx = np.where((nama_np == cari) | (kode_np == cari))[0]

        if len(idx) > 0:
            i = idx[0]

            # remove
            nama.pop(i)
            kode.pop(i)
            jumlah.pop(i)
            harga.pop(i)

            print("Barang berhasil dihapus")
        else:
            print("Barang tidak ditemukan")

    # search
    elif pilih == "3":
        cari = input("Masukkan nama atau kode barang: ")

        nama_np = np.array(nama)
        kode_np = np.array(kode)

        # find
        idx = np.where((nama_np == cari) | (kode_np == cari))[0]

        if len(idx) > 0:
            i = idx[0]
            print("\nBarang ditemukan")
            print("Nama:", nama[i])
            print("Kode:", kode[i])
            print("Jumlah:", jumlah[i])
            print("Harga:", harga[i])
            print("Total:", jumlah[i] * harga[i])
        else:
            print("Barang tidak ditemukan")

    # exit
    elif pilih == "4":
        print("Program selesai")
        break

    # error
    else:
        print("Menu tidak valid")

# Program dimulai dengan menyiapkan tempat penyimpanan data barang (nama, kode, jumlah, harga)

# Program masuk ke loop menu agar user bisa menjalankan fitur berulang kali

# User memilih menu dari CLI

# Jika memilih input:
# Data barang dimasukkan oleh user lalu disimpan ke dalam list

# Jika memilih delete:
# Program mencari barang berdasarkan nama atau kode
# Jika ditemukan, data barang dihapus dari penyimpanan

# Jika memilih search:
# Program mencari barang di data yang tersimpan
# Jika ditemukan, detail barang dan total harga ditampilkan

# Jika memilih keluar:
# Program menghentikan loop dan selesai
