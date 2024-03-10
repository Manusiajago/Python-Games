# memnaggil library random untuk membangkitkan bilangan acak
import random

welcome_message = "WELCOME TO PYTHON !"
posisi_maskot = random.randint(1, 4)

print("===============================")
print(f'''=== {welcome_message} =======''')
print("===============================")




nama_pengguna = input(" Masukkan nama kamu : ")

bentuk_goa = "|_|"
goa_kosong = [bentuk_goa] * 4  # ini harus tetap kosong
goa = goa_kosong.copy() # tempat baru python
goa[posisi_maskot - 1 ] = "|0_0|" # perilaku random python dikurang 1
result_string = ''.join(map(str, goa))
new_goa_kosong = ''.join(map(str, goa_kosong))

print(f'''
 Halo selamat datang {nama_pengguna} ! Coba perhatikan GOA dibawah ini !
 {new_goa_kosong}
''')

# fungsi int untuk mengkonversi string menjadi integer/number

pilihan_pengguna = int(input(" Menurut kamu di GOA nomor berapa Python berada ? [ 1 / 2 / 3 / 4 ] "))

# menambahkan konfirmasi 
konfirmasi_user = input(f"Apakah anda yakin memilih {pilihan_pengguna} ? [y/n] ").lower()


if konfirmasi_user == "n":
    print(" Program dihentikan / dibatalkan ! ")
    exit()
elif konfirmasi_user == "y":
    if pilihan_pengguna == posisi_maskot : 
        print(f" Yes kamu benar pilihan kamu adalah {pilihan_pengguna} dan Python berada di goa nomer -> {posisi_maskot} \n {result_string}")
    else : 
        print(f" Kamu kalah karena posisi Python berada di nomer -> {posisi_maskot} \n {result_string}")
else : 
    print(" pilihan di batalkan , masukkan pilihan dengan sesuai ! ")
    exit()