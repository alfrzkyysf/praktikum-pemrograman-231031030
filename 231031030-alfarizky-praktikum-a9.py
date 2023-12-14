import os

def judul():
    print('PROGRAM MEGHITUNG LUAS DAN KELILING'.center(45))
print('PROGRAM MENGHITUNG LUAS DAN KELILING'.center(45))
print('BANGUN DATAR PERSEGI'.center(45))
print()

def inputan():
    panjang = float(input('masukkan panjang: '))
    lebar = float(input('masukkan lebar: '))
    return panjang,lebar


def hitung(panjang,lebar):
    luas = panjang*lebar
    kel = (panjang*lebar)*2
    return luas,kel

def tampil(pesan,nilai):
    print(f'hasil perhitungan nilai {pesan}: {nilai}')

def pilihan():
    pilih = input('apakah ingin melanjutkan? [y/n]')
    if pilih == 'y':
        a = True
    else:
        a = False
        print('sampai jumpa.')
    return a

a = True
while a:
    # judul
    print()

    # inputan panjang dan lebar
    panjang,lebar = inputan()

    #hitung
    luas,kel = hitung(panjang,lebar) 

    # cetak atau display 
    tampil('luas',luas)
    tampil('keliling',kel)
    
    # pilihan
    a = pilihan()