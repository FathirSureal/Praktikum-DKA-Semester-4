import numpy as np

# variable
nama = []
nilai = np.array([]).reshape(0,3)

# input
def input_data():
    global nama, nilai
    n = int(input("Jumlah mahasiswa: "))
    for i in range(n):
        nma = input("Nama: ")
        t = float(input("Tugas: "))
        uts = float(input("UTS: "))
        uas = float(input("UAS: "))
        nama.append(nma)
        nilai = np.vstack([nilai, [t, uts, uas]])

# tampil
def tampil_array():
    print(nilai)

# nilai akhir
def nilai_akhir():
    na = (0.3 * nilai[:,0]) + (0.3 * nilai[:,1]) + (0.4 * nilai[:,2])
    for i in range(len(nama)):
        print(nama[i], ":", na[i])

# analisis
def analisis():
    na = (0.3 * nilai[:,0]) + (0.3 * nilai[:,1]) + (0.4 * nilai[:,2])
    print("Rata-rata:", np.mean(na))
    print("Median:", np.median(na))
    print("UAS > median NA:")
    for i in range(len(nama)):
        if nilai[i][2] > np.median(na):
            print(nama[i])

# top3
def top3():
    na = (0.3 * nilai[:,0]) + (0.3 * nilai[:,1]) + (0.4 * nilai[:,2])
    idx = np.argsort(na)[-3:][::-1]
    for i in idx:
        print(nama[i], na[i])

# cari
def cari():
    nma = input("Cari nama: ")
    if nma in nama:
        i = nama.index(nma)
        print(nma, nilai[i])
    else:
        print("Tidak ada")

# update
def update():
    nma = input("Nama: ")
    if nma in nama:
        i = nama.index(nma)
        t = float(input("Tugas baru: "))
        uts = float(input("UTS baru: "))
        uas = float(input("UAS baru: "))
        nilai[i] = [t, uts, uas]
    else:
        print("Tidak ada")

# hapus
def hapus():
    global nama, nilai
    nma = input("Nama: ")
    if nma in nama:
        i = nama.index(nma)
        nama.pop(i)
        nilai = np.delete(nilai, i, axis=0)
    else:
        print("Tidak ada")

# menu
while True:
    print("\n1.Input\n2.Tampil\n3.Nilai Akhir\n4.Analisis\n5.Top 3\n6.Cari\n7.Update\n8.Hapus\n9.Keluar")
    p = input("Pilih: ")
    if p == "1":
        input_data()
    elif p == "2":
        tampil_array()
    elif p == "3":
        nilai_akhir()
    elif p == "4":
        analisis()
    elif p == "5":
        top3()
    elif p == "6":
        cari()
    elif p == "7":
        update()
    elif p == "8":
        hapus()
    elif p == "9":
        break

#NumPy dua dimensi untuk nilai.

#Saat program dijalankan, user akan melihat menu utama yang berisi berbagai pilihan fitur.
#1. Jika user memilih input, program akan meminta jumlah mahasiswa yang ingin dimasukkan.
#   Setelah itu, program meminta nama, nilai tugas, nilai UTS, dan nilai UAS satu per satu.
#   Setiap data yang dimasukkan akan langsung disimpan, nama masuk ke dalam list dan nilai masuk ke dalam array.

#2. Jika user memilih tampilkan data, program akan menampilkan seluruh isi array nilai yang sudah tersimpan.

#3. Ketika user memilih menghitung nilai akhir, program akan mengambil setiap baris nilai dan menghitungnya dengan rumus yang sudah ditentukan.
#   Hasil nilai akhir kemudian ditampilkan berdampingan dengan nama mahasiswa masing-masing.

#4. Jika user masuk ke menu analisis, program akan menghitung rata-rata dari semua nilai akhir yang ada.
#   Program juga menghitung median untuk melihat nilai tengah dari keseluruhan data.
#   Setelah itu, program akan membandingkan nilai UAS setiap mahasiswa dengan median nilai akhir untuk mencari siapa saja yang memenuhi kriteria.

#5. Ketika user memilih fitur top 3, program akan mengurutkan nilai akhir dari yang terendah ke tertinggi.
#   Lalu program mengambil tiga nilai tertinggi dan menampilkan nama beserta nilainya.

#6. Jika user ingin mencari data, program akan meminta nama mahasiswa yang dicari.
#   Program kemudian mencocokkan nama tersebut dengan data yang ada dan menampilkan hasilnya jika ditemukan.

#7. Jika user ingin memperbarui nilai, program akan meminta nama mahasiswa lalu mengganti nilai lama dengan nilai baru yang diinput.
#   Perubahan tersebut langsung disimpan di dalam array tanpa membuat data baru.

#8. Jika user memilih hapus, program akan mencari nama mahasiswa yang dimaksud lalu menghapusnya dari list dan array.
#   Data yang sudah dihapus tidak akan muncul lagi di sistem.
#Semua proses ini berjalan berulang di dalam menu sampai user memilih keluar.
