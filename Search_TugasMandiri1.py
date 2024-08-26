list = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 
       1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900, 
       3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900, 4000, 4100, 4200, 4300, 4400, 4500, 
       4600, 4700, 4800, 4900, 5000, 5100, 5200, 5300, 5400, 5500, 5600, 5700, 5800, 5900, 6000, 6100, 6200, 
       6300, 6400, 6500, 6600, 6700, 6800, 6900, 7000, 7100, 7200, 7300, 7400, 7500, 7600, 7700, 7800, 7900, 8000, 
       8100, 8200, 8300, 8400, 8500, 8600, 8700, 8800, 8900, 9000, 9100, 9200, 9300, 9400, 9500, 9600, 9700, 9800, 9900, 10000]
       # bilangan yang akan diurutkan
print("LIST DATA: ")
print(list) # menampilkan bilangan sebelum diurutkan
cari = int(input("Masukkan nilai yang dicari: ")) # input nilai yang dicari

def interpolar_search(list, cari): # Fungsi interpolar search dengan parameter list dan cari
    kiri = 0 # Tentukan batas bawah
    kanan = len(list) - 1 # Tentukan batas atas
    iterasi = 0 # variabel iterasi awal
    
    while kiri <= kanan and cari >= list[kiri] and cari <= list[kanan]: # Selama batas bawah tidak melebihi batas atas
        iterasi += 1 # Tambahkan iterasi
        tengah = kiri + ((kanan - kiri) // (list[kanan] - list[kiri])) * (cari - list[kiri]) 
        # Temukan indeks tengah dengan rumus interpolasi
        if list[tengah] == cari: # Jika elemen ditemukan
            return tengah, iterasi # Mengembalikan indeks jika elemen ditemukan
        elif list[tengah] < cari: # Jika indeks tengah lebih kecil dari target
            kiri = tengah + 1 # Tentukan batas bawah dengan indeks tengah ditambah 1
        else: # Jika indeks tengah lebih besar dari target
            kanan = tengah - 1 # Tentukan batas atas dengan indeks tengah dikurangi 1
    return -1, iterasi # Mengembalikan -1 jika elemen tidak ditemukan

hasil, iterasi = interpolar_search(list, cari) # Memanggil fungsi interpolar_search

if hasil != -1: # Jika elemen ditemukan
    print(f"Elemen ditemukan di indeks ke-{hasil} setelah {iterasi} iterasi") # Menampilkan indeks elemen
else: # Jika elemen tidak ditemukan
    print(f"Elemen tidak ditemukan setelah {iterasi} iterasi")
    