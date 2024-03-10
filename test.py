#cara untuk menerjemahkan urutan index secara manusia  
myhobby = ["bertinju" , "ngoding" , "main bola"]
start_from = 1 

print(myhobby[1 - start_from])

#cara untuk memunculkan isi nilai array , best practice
mahasiswa = ["Egal Assegaf" , 23 , "Teknik Informatika" , "Universitas Indraprastra PGRI"]
print(mahasiswa[0])
print(mahasiswa[1])
print(mahasiswa[3])

# cara menimpa/menggati isi array dengan cara menambahkan variabel baru
buahBuahan = ["nanas" , "anggur" , "pisang" , "semangka" , "nangka" , "melon" , "apel" , "mangga"]

#temukan data terakhir & timpa data tersebut menjadi nama anda
buahBuahan[7] = "jeruk"
print(buahBuahan[len(buahBuahan) - 1])
 







# print(f" ini hasil dari variabel -> buahBuahan {buahBuahan}")

# copy_buah = buahBuahan

# copy_buah[1] = "susu"
# print(f" Ini hasil dari copy_buah -> {copy_buah}")