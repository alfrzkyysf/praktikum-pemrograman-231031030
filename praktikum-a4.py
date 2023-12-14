import os
os.system('clear')

nim = ['2','3','1','0','3','1','0','3','0']
# nim2 = '231031029'
print(nim[1:3])
# print(nim2[1:3])

# akses item
print(f'item indeks 0:{nim[0]}')
print(f'item indeks 4:{nim[4]}')
print(f'item indeks terakhir: {nim[len(nim)-1]}')

# akses indeks negatif
print(f'item indeks terakhir: {nim[-1]}')
print(f'item indeks terakhir: {nim[-len(nim)]}')
print(f'item indeks 6 [-1]: {nim[-3]}')
print(f'item indeks 4 [-5]: {nim[-5]}')
print(f'item indeks 7 [-2]: {nim[-2]}')

# akses indeks batas
print(f'item indeks 1,2,...: \n {nim[1:]}')
print(f'item indeks 3,4,...: \n {nim[3:]}')
print(f'item indeks 0,1,2,: \n {nim[:3]}')
print(f'item indeks 0,1,2,3: \n {nim[:4]}')
print(f'item indeks semua: \n {nim[:]}')
print(f'item indeks [:8]: \n {nim[:-1]}')
print(f'item indeks [:6]: \n {nim[:-3]}')

# pengirisan 
print(f'item indeks 1,2 : \n {nim[1:3]}')
print(f'item indeks 2,3,4: \n {nim[2:5]}')
print(f'item indeks kosong: \n {nim[3:3]}')
print(f'item indeks [8:8] kosong : \n {nim[-1:-1]}')
print(f'item indeks [1:8]: \n {nim[1:-1]}')
print(f'item indeks [2:7]: \n {nim[2:-2]}')

data = ['muhammad alfarizky yusuf',2023,'Aktif']
nilai= [90,89,93,97]

# tugas 1 list
print('Nama: '+ data[0])
print('angkatan:', data[1])
print('status: '+ data[2])

print(f'{data[0]} status kuliah : {data[2]}')
print(f'data terbesar nilai adalah: {nilai[-1]}')
print(f'data terkecil nilai adalah: {nilai[1]}')
print(f'rata rata nilai adalah {sum(nilai)/len(nilai)}')

# tugas 2 tuple
data = ('nugrah',2023,'Aktif')
nilai= (90,89,93,97)

print(data[1])
print(data[-1])
print(nilai[1:-1])


print(f' jumlah nilai alfarizky adalah: {len(nilai)}')
print(f'data terbesar nilai adalah: {nilai[-1]}')
print(f'data terkecil nilai adalah: {nilai[1]}')
print(f'rata rata nilai adalah {sum(nilai)/len(nilai)}')

# latihan nested list
data = [('alfarizky',2023,'Aktif'),
        (90,89,93,97),
        (20,22),
        ('S1-Reguler','Ganjil')]

print(data[0][0])
print(data[-1][0])
print(data[2][0:])

print(f'\nProgram pendidikan {data[0][0]}: {data[3][0]}\n')
print(f'Angkatan {data[0][1]}-{data[3][1]}\n')
print(f'Jumlah Nilai {data[0][0]} : adalah : {len(data[1])}\n')
print(f'Data tebesar {data[0][0]} adalah : {max(data[1])}\n')
print(f'Data terkecil nilai adalah : {min(data[1])}\n')
print(f'rata-rata nilai nilai adalah : {sum(data[1])/len(data[1])}\n')

matkul = []

