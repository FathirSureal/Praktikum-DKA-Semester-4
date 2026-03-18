import numpy as np
import random
#  variable
nama = []
kode = []
data = np.array([]).reshape(0,2)
np.set_printoptions(suppress=True, precision=0)

# input
def input_data():
    global data
    n = int(input("Jumlah pelanggan: "))
    for i in range(n):
        nma = input("Nama: ")
        tb = int(input("Total Belanja: "))
        jt = int(input("Jumlah Transaksi: "))
        
        kd = "UND-" + str(random.randint(1000,9999))
        
        nama.append(nma)
        kode.append(kd)
        data = np.vstack([data, [tb, jt]])

# tampil
def tampil():
    for i in range(len(nama)):
        print(nama[i], kode[i], data[i])

# rata
def rata():
    print("Rata-rata:", np.mean(data[:,0]))

# prioritas
def prioritas():
    avg = np.mean(data[:,0])
    for i in range(len(nama)):
        if data[i][0] > avg:
            print(nama[i])

# peserta
def peserta():
    idx = []
    for i in range(len(nama)):
        if data[i][1] >= 3:
            idx.append(i)
    return idx

# slot
def slot(i, avg):
    tb = data[i][0]
    s = 0
    if tb < 300000:
        s = 1
    elif tb <= 700000:
        s = 2
    else:
        s = 3
    if tb > avg:
        s += 2
    return s

# undi
def undi():
    idx = peserta()
    avg = np.mean(data[:,0])
    
    pool = []
    
    for i in idx:
        s = slot(i, avg)
        for j in range(s):
            pool.append(i)
    
    if len(pool) < 2:
        print("Peserta kurang")
        return
    
    pemenang = random.sample(list(set(pool)), 2)
    
    for i in pemenang:
        print("Menang:", nama[i], kode[i])

# cari
def cari():
    kd = input("Kode: ")
    if kd in kode:
        i = kode.index(kd)
        print(nama[i], data[i])
    else:
        print("Tidak ada")

# menu
while True:
    print("\n1.Input\n2.Tampil\n3.Rata\n4.Prioritas\n5.Undi\n6.Cari\n7.Keluar")
    p = input("Pilih: ")
    
    if p == "1":
        input_data()
    elif p == "2":
        tampil()
    elif p == "3":
        rata()
    elif p == "4":
        prioritas()
    elif p == "5":
        undi()
    elif p == "6":
        cari()
    elif p == "7":
        break
