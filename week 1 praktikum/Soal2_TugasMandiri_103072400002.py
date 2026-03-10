# program konversi suhu dari celsius
# input suhu
celsius = float(input("Masukkan suhu dalam Celsius: "))

# konversi
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

# hasil
print("\n Konversi ")
print("Fahrenheit :", format(fahrenheit, ".2f"))
print("Kelvin :", format(kelvin, ".2f"))

#Langkah pertama yang dilakukan program adalah meminta pengguna memasukkan nilai suhu dalam Celsius. 
#Input ini kemudian disimpan dalam variabel celsius. Karena suhu dapat berupa angka desimal, program menggunakan float() agar data bisa diproses sebagai bilangan desimal.

#Setelah suhu dalam Celsius diterima, program mulai melakukan proses konversi suhu.

#Nilai Celsius dikalikan dengan 9/5, kemudian hasilnya ditambahkan dengan 32. Hasil perhitungan ini disimpan dalam variabel fahrenheit.

#Nilai Celsius hanya perlu ditambahkan dengan 273.15. Hasilnya disimpan dalam variabel kelvin.

#Setelah kedua nilai konversi didapatkan, program menampilkan hasilnya ke layar.
