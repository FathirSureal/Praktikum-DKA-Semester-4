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

#NumPy dua dimensi untuk data pelanggan (TotalBelanja dan JumlahTransaksi).

#Saat program dijalankan, user akan melihat menu utama yang berisi berbagai pilihan fitur.

#1. Jika user memilih input, program akan meminta jumlah pelanggan yang ingin dimasukkan.
#   Setelah itu, program meminta nama, total belanja, dan jumlah transaksi satu per satu.
#   Program juga membuat kode undian otomatis dengan format UND-XXXX.
#   Setiap data yang dimasukkan akan langsung disimpan, nama dan kode masuk ke dalam list dan data numerik masuk ke dalam array.

#2. Jika user memilih tampilkan data, program akan menampilkan seluruh data pelanggan yang sudah tersimpan.

#3. Jika user memilih rata-rata, program akan menghitung rata-rata total belanja dari seluruh pelanggan menggunakan NumPy.

#4. Jika user memilih prioritas, program akan membandingkan total belanja setiap pelanggan dengan rata-rata.
#   Pelanggan dengan total belanja lebih besar dari rata-rata akan ditampilkan sebagai pelanggan prioritas.

#5. Program menentukan peserta undian dengan mengecek jumlah transaksi.
#   Hanya pelanggan dengan jumlah transaksi minimal 3 yang dapat mengikuti undian.

#6. Program menentukan jumlah slot undian berdasarkan total belanja.
#   Jika total belanja kurang dari 300.000 maka mendapat 1 slot.
#   Jika total belanja antara 300.000 sampai 700.000 maka mendapat 2 slot.
#   Jika total belanja lebih dari 700.000 maka mendapat 3 slot.
#   Jika pelanggan termasuk prioritas, maka akan mendapatkan tambahan 2 slot.

#7. Ketika user memilih undi, program akan mengumpulkan semua slot undian ke dalam satu pool.
#   Semakin banyak slot, semakin besar peluang untuk menang.
#   Program kemudian memilih 2 pemenang secara acak tanpa ada pemenang yang sama.

#8. Jika user ingin mencari data, program akan meminta kode undian pelanggan.
#   Program kemudian mencocokkan kode tersebut dengan data yang ada dan menampilkan hasilnya jika ditemukan.

#Semua proses ini berjalan berulang di dalam menu sampai user memilih keluar.
