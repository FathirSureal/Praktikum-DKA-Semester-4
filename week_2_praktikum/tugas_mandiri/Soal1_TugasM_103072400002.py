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
