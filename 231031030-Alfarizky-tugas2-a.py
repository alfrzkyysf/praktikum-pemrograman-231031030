try:
    def tambah_waktu(waktu_awal, jam_tambahan, menit_tambahan):
        # Memisahkan waktu awal menjadi jam dan menit
        jam_awal, menit_awal = map(int, waktu_awal.split(':'))

        # Menambahkan jam dan menit tambahan
        jam_baru = (jam_awal + jam_tambahan + (menit_awal + menit_tambahan) // 60) % 24
        menit_baru = (menit_awal + menit_tambahan) % 60

        # Mengubah hasil ke format waktu yang sesuai
        waktu_baru = f"{jam_baru:02d}:{menit_baru:02d}"

        return waktu_baru

    # Input waktu awal
    waktu_awal = input("Masukkan waktu awal (hh:mm): ")
    jam_tambahan = int(input("Masukkan jumlah jam tambahan: "))
    menit_tambahan = int(input("Masukkan jumlah menit tambahan: "))

    # Memanggil fungsi tambah_waktu
    waktu_sekarang = tambah_waktu(waktu_awal, jam_tambahan, menit_tambahan)

    # Menampilkan waktu sekarang
    print(f"Waktu sekarang menunjukkan Pukul {waktu_sekarang}")
except ValueError:
    print('masukan format yang benar') 