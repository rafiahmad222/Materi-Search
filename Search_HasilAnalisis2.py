# Deskripsi: Mencari elemen dalam array menggunakan algoritma pencarian linear dan binary
list = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400,] # bilangan yang akan diurutkan
target = 10 # bilangan yang akan dicari
print('---Linear Search---') 
def linear(list, target): # Fungsi linear search dengan parameter list dan target
    iterasi = 0  # variabel iterasi awal
    for i in range(len(list)): # Perulangan untuk setiap elemen dalam list
        iterasi += 1 # Tambahkan iterasi
        if list[i] == target: # Jika elemen ditemukan
            return i, iterasi # Mengembalikan indeks jika elemen ditemukan
    return -1, iterasi # Mengembalikan -1 jika elemen tidak ditemukan

hasil, iterasi = linear(list, target) # Memanggil fungsi linear
if hasil != -1: # Jika elemen ditemukan
    print(f"Elemen ditemukan di indeks ke-{hasil} setelah {iterasi} iterasi") # Menampilkan indeks elemen
else:
    print(f"Elemen tidak ditemukan setelah {iterasi} iterasi")
    
print('---Binary Search---') 
def binary(list, target): # Fungsi binary search dengan parameter list dan target
    left = 0 # Tentukan batas bawah
    right = len(list) - 1 # Tentukan batas atas
    iterasi = 0 # variabel iterasi awal
    while left <= right: # Selama batas bawah tidak melebihi batas atas
        mid = (left + right) // 2 # Temukan indeks tengah dengan menambahkan batas bawah dan atas lalu dibagi 2
        iterasi += 1 # Tambahkan iterasi
        if list[mid] == target: # Jika indeks tengah sama dengan target
            return mid, iterasi # Mengembalikan indeks jika elemen ditemukan
        elif list[mid] < target: # Jika indeks tengah lebih kecil dari target
            left = mid + 1 # Tentukan batas bawah dengan indeks tengah ditambah 1
        else:   # Jika indeks tengah lebih besar dari target
            right = mid - 1 # Tentukan batas atas dengan indeks tengah dikurangi 1
    return -1, iterasi # Mengembalikan -1 jika elemen tidak ditemukan

hasil, iterasi = binary(list, target) # Memanggil fungsi binary
if hasil != -1: # Jika elemen ditemukan
    print(f"Elemen ditemukan di indeks ke-{hasil} setelah {iterasi} iterasi") # Menampilkan indeks elemen
else:
    print(f"Elemen tidak ditemukan setelah {iterasi} iterasi")