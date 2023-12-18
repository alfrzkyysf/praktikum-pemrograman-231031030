#Fungsi Rekursif factorial dengan perulangan
def faktorial(nilai):
 if nilai<=1:
    return 1
 else:
    return nilai*faktorial(nilai-1)
#Program Utama
for i in range(11):
 print('%2d ! = %d' % (i,faktorial(i)))
 0 ! = 1
 1 ! = 1
 2 ! = 2
 3 ! = 6
 4 ! = 24
 5 ! = 120
 6 ! = 720
 7 ! = 5040
 8 ! = 40320
 9 ! = 362880
10 ! = 3628800
#Fungsi Rekursif Fibonacci
def fibonacci(n):
 if n<0:
    print('Tidak ada bilangan yang bernilai negatif')
 if n==0 or n==1:
    return n
 else:
    return fibonacci(n-1) + fibonacci(n-2)
#Program Utama
hasil=fibonacci(21)
print(hasil)