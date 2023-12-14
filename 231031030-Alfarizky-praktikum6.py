# Inisialisasi variabel a dengan nilai True
a = True

# Memulai loop while dengan kondisi a
while a:
    # Mengambil input dari pengguna dengan pesan 'Apakah kamu bukan robot? (iya/tidak)'
    jawab = input('Apakah kamu bukan robot? (iya/tidak)')
    
    # Jika jawabannya 'iya'
    if jawab =='iya':
        # Mencetak 'Halo Tuanku!' ke layar
        print('Halo Tuanku!')
        # Mengubah nilai a menjadi False untuk mengakhiri loop
        a = False
    
    # Jika jawabannya 'tidak'
    elif jawab =='tidak':
        # Mencetak 'Kamu Bukan Temanku:D' ke layar
        print('Kamu Bukan Temanku:(')
        # Mengubah nilai a menjadi False untuk mengakhiri loop
        a = False
    
    # Jika jawaban tidak 'iya' atau 'tidak'
    else:
        # Mencetak 'Maaf gak kenal:.))' ke layar
        print('Maaf gak kenal:.)')
        # Mengatur a ke True agar loop terus berjalan dan meminta input lagi
        a = True