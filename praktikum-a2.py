print('praktikum-a2\n\n')

print('NAMA    :MUHAMMAD ALFARIZKY YUSUF')
print('NIM     :231031030')
print('Prodi   :Sistem Informasi A\n')

# INI OPERATOR ASSIGNMENT
a = 19
print('Nilai a adalah',a)
a += 3
print('Nilai a+=3 adalah',a)

a = 19
print('Nilai a adalah',a)
a -= 3
print('Nilai a-=3 adalah',a)

a = 19
print('Nilai a adalah',a)
a *= 2
print('Nilai a*=2 adalah',a)

a = 19
print('Nilai a adalah',a)
a /= 2
print('Nilai a/=2 adalah',a)

a = 3
print('Nilai a adalah',a)
a **= 2
print('Nilai a**=2 adalah',a)

a = 35
print('Nilai a adalah',a)
a //= 32
print('Nilai a//=32 adalah',a)

# Tugas melanjutkan untuk operator selanjutnya line 25-59
# Operator perbandingan
a = 9
b = 13
print('\n------- Besar dari 30')
hasil = a > 30
print(a,'> 30 adalah',hasil)
hasil = b > 30
print(b,'> 30 adalah',hasil)


hasil = a < 30
print(a,'< 30 adalah',hasil)
hasil = b < 30
print(b,'< 30 adalah',hasil)


# Tugas
print('\n------- Kecil dari 30')
# hasil = a >= 30
# hasil = a >= 30


# Tugas
print('\n------- Kecil dari 30')
# hasil = a <= 30
# hasil = a <= 30


# Tugas
print('\n------- Kecil dari 30')
# hasil = a == 30
# hasil = a == 30


# Tugas
print('\n------- Kecil dari 30')
# hasil = a != 30
# hasil = a != 30

# OPERATOR LOGIKA
a = True
b = False
print('\n=======AND=======')
hasil = a and a
print(a,'and',a,'hasilnya=',hasil)

hasil = a and b
print(a,'and',b,'hasilnya=',hasil)

hasil = b and a
print(b,'and',a,'hasilnya=',hasil)

hasil = b and b
print(b,'and',b,'hasilnya=',hasil)

print('\n=======OR=======')
# Tugas
# hasil = a or a
# hasil = a or b
# hasil = b or a
# hasil = b or b

print('\n=======XOR=======')
hasil = a ^ a
print(a,'xor',a,'hasilnya =',hasil)

hasil = a ^ b
print(a,'xor',b,'hasilnya =',hasil)

hasil = b ^ a
print(b,'xor',a,'hasilnya =',hasil)

hasil = b ^ b
print(b,'xor',b,'hasilnya =',hasil)

print('\n=======NOT======='
      )
hasil = not a
print('not',a,'hasilnya =',hasil)

hasil = not b
print('not',b,'hasilnya =',hasil)

# OPERATOR MEMBERSHIP
print('\n===========IN')
nama = 'Alfarizky'
test = 'iz'
cek = test in nama
print(test,'terdapat di',nama,'adalah',cek)

test = 'zi'
cek = test in nama
print(test,'terdapat di',nama,'adalah',cek)

test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'

cek = test1 in nama
print(test1,'terdapat di',nama,'adalah',cek)

cek = test2 in nama
print(test2,'terdapat di',nama,'adalah',cek)

cek = test3 in nama
print(test3,'terdapat di',nama,'adalah',cek)

cek = test4 in nama
print(test4,'terdapat di',nama,'adalah',cek)

cek = test5 in nama
print(test5,'terdapat di',nama,'adalah',cek)

print('\n===========NOT IN')
# Tugas Lanjutkan untuk NOT IN dengan cara yang sama




