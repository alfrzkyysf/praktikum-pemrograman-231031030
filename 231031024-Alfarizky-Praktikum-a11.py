#Fungsi Rekursif Fibonacci
def fibonacci(n):
 if n<0:
    print('Tidak ada bilangan yang bernilai negatif')
 if n==0 or n==1:
    return n
 else:
    return fibonacci(n-1) + fibonacci(n-2)
#Program Utama
hasil=fibonacci(20)
print(hasil)

#Fungsi Rekursif Fibonacci yang akan menerima input
def fibonacci(n):
 if n<0:
    print('Tidak ada bilangan yang bernilai negatif')
 if n==0 or n==1:
    return n
 else:
    return fibonacci(n-1) + fibonacci(n-2)
#Program Utama
fib = fibonacci(int(input("masukkan sebuah bilangan: ")))
# hasil=fibonacci(20)
print(fib)
