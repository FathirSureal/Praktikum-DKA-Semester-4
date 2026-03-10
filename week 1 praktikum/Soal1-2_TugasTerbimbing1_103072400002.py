#  kabisat
def isKabisat(tahun):
    if (tahun % 400 == 0) or (tahun % 4 == 0 and tahun % 100 != 0):
        return True
    return False

# fibonacci 
def fibonacci(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

# cetak 
def cetak_fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# input 
tahun = int(input("Masukkan tahun: "))

# hasil 
print(isKabisat(tahun))

# input 
n = int(input("Masukkan n: "))

# fibonacci 
print("Fibonacci ke-", n, "=", fibonacci(n))

# deret 
cetak_fibonacci(n)
