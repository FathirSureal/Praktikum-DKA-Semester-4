# program menghitung nilai akhir mahasiswa
# input data
nama = input("Masukkan nama mahasiswa: ")
nilai_tugas = float(input("Masukkan nilai tugas: "))
nilai_uts = float(input("Masukkan nilai UTS: "))
nilai_uas = float(input("Masukkan nilai UAS: "))

# hitung nilai akhir
nilai_akhir = (nilai_tugas * 0.20) + (nilai_uts * 0.35) + (nilai_uas * 0.45)

# tampilkan 
print("\n Hasil Nilai")
print("Nama Mahasiswa :", nama)
print("Nilai Akhir :", nilai_akhir)

#Pertama, program menjalankan fungsi input() untuk mengambil nama mahasiswa dan menyimpannya di variabel nama.Karena nama adalah teks, maka data tersebut otomatis disimpan sebagai string.

#Selanjutnya program meminta nilai tugas, nilai UTS, dan nilai UAS.Nilai yang dimasukkan awalnya berbentuk string, sehingga program menggunakan float() untuk mengubahnya menjadi angka desimal agar bisa dihitung secara matematis.

#Setelah semua data diterima, program mulai mengolah nilai.Program menghitung nilai akhir menggunakan bobot yang telah ditentukan

#Terakhir, program menampilkan hasilnya ke layar.
