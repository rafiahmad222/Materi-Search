list = [1, 2, 2, 5, 9, 13, 14, 17] # list angka
selisih = 3 # selisih angka

def cari_pasangan(list, selisih): # fungsi cari pasangan angka
    pasangan = 0 # variabel pasangan
    angka = [] # variabel angka
    
    for i in range(len(list)): # perulangan pertama untuk mengecek bilangan pertama
        for j in range(i+1, len(list)): # perulangan kedua untuk mengecek bilangan kedua
            if abs(list[i] - list[j]) == selisih: # jika selisih bilangan pertama dan kedua sama dengan selisih maka menjalankan perintah dibawah
                pasangan += 1 # menambahkan pasangan
                angka.append((list[i], list[j])) # menambahkan angka ke dalam variabel angka
                
    return pasangan, angka # mengembalikan pasangan dan angka

hasil, angka = cari_pasangan(list, selisih) # memanggil fungsi cari pasangan

print(f"Ada {hasil} pasangan angka yang memiliki selisih {selisih}") # menampilkan hasil
print(angka) # menampilkan angka



