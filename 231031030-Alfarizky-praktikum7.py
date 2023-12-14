pw_benar = 'parri14'
percobaan = 3
a = True 
while a:
    masukan = input('masukkan password: ')
    if masukan == pw_benar:
        print('selamat datang di welcome!')
        a = False
    else:
        if percobaan == 0:
            print('password anda salah! akun anda di banned')
            a = False
        else:
            print('password anda salah! coba lagi dengan sisa percobaan: ', percobaan)
            percobaan -= 1