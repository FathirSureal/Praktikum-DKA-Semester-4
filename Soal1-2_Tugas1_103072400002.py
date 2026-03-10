# cek kabisat
def isKabisat(tahun):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        return True
    return False


# fibonacci n
def fibonacci(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b


# cetak deret
def cetak_fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()


# input tahun
tahun = int(input("Masukkan tahun: "))

# hasil kabisat
print(isKabisat(tahun))


# input n
n = int(input("Masukkan n: "))

# fibonacci ke-n
print("Fibonacci ke-", n, "=", fibonacci(n))

# deret fibonacci
cetak_fibonacci(n)
