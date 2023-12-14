try:
    JAM_awal = input("Masukkan JAM awal (Contoh: 12:00) : ")
    jam, menit = map(int, JAM_awal.split(':'))

    jam_kurang = int(input("Masukkan jumlah jam yang akan dikurangkan (Contoh: 2): "))
    menit_kurang = int(input("Masukkan jumlah menit yang akan dikurangkan (Contoh: 30) : "))

    jam_akhir = (jam - jam_kurang - (menit - menit_kurang) // 60) % 24
    menit_akhir = (menit - menit_kurang) % 60

    JAM_akhir = f'{jam_akhir:02d}:{menit_akhir:02d}'

    print(f'JAM sekarang menunjukkan Pukul {JAM_akhir}')
except ValueError:
    print('Mohon masukkan format jam dengan benar!')