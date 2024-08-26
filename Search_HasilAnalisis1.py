arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # bilangan yang akan diurutkan
target = 6 # bilangan yang akan dicari

def binary_search(arr, target): # Fungsi binary search dengan parameter arr dan target
    low, high = 0, len(arr) - 1 # Tentukan batas bawah dan atas
    iterasi = 0 # Inisialisasi variabel iterasi

    while low <= high: # Selama batas bawah tidak melebihi batas atas
        mid = (low + high) // 2  # Temukan indeks tengah
        iterasi += 1 # Tambahkan iterasi
        print(f"Iterasi:{iterasi} low={low}, high={high}, mid={mid}, arr[mid]={arr[mid]}")

        if arr[mid] == target: # Jika elemen ditemukan
            return mid, iterasi  # Mengembalikan indeks jika elemen ditemukan
        elif arr[mid] < target:
            low = mid + 1  # Cari di setengah kanan array
        else:
            high = mid - 1  # Cari di setengah kiri array

    return -1, iterasi  # Mengembalikan -1 jika elemen tidak ditemukan

hasil, iterasi = binary_search(arr, target) # Memanggil fungsi binary_search

if hasil != -1: # Jika elemen ditemukan
    print(f"Elemen ditemukan di indeks ke-{hasil} setelah {iterasi} iterasi") # Menampilkan indeks elemen
else:
    print("Elemen tidak ditemukan setelah {iterasi} iterasi")