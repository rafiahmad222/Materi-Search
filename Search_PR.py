data = "Semoga semoganya disemogakan dan cepat tersemogakan, karena semoga harus disemogakan"
target = "semoga"

def linear_search(data, target):
    for i in range(len(data)):
        if data[i:i+len(target)] == target:
            return i
    return -1

hasil = linear_search(data, target)

if hasil != -1:
    print(f"Kata kunci {target} ditemukan pada indeks ke-{hasil}")
else:
    print(f"Kata kunci {target} tidak ditemukan")
    
# target = int(input("Masukkan bilangan yang ingin dicari: "))
# ucok = int(input("Masukkan bilangan yang terpikirkan oleh Ucok: "))
# for i in range(ucok):
#     if i == 0:
#         data = [i]
#     else:
#         data.append(i)
# data = []

# def binary_search(data, target):
#     low = 0
#     high = len(data) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         if data[mid] == target:
#             return mid
#         elif data[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1


# # soal 3
# import time
# def bubble_sort(data):
#     for i in range(len(data)):
#         for j in range(len(data) - 1):
#             if data[j] > data[j + 1]:
#                 data[j], data[j + 1] = data[j + 1], data[j]
#     return data

# def binary_search(data, target):
#     bawah = 0
#     atas = len(data) - 1
#     while bawah <= atas:
#         tengah = (bawah + atas) // 2
#         if data[tengah] == target:
#             return tengah
#         elif data[tengah] < target:
#             bawah = tengah + 1
#         else:
#             atas = tengah - 1
#     return -1


# start_time = time.time()
# data = [2, 1, 4, 5, 6, 3, 101, 14141, 9, 7]
# target = int(input("Masukkan target: "))
# sorted_data = bubble_sort(data)
# print(sorted_data)    
# hasil = binary_search(sorted_data, target)
# if hasil != -1:
#     print(f"Target {target} ditemukan pada index:", hasil)
# else:
#     print(f"Target {target} tidak ditemukan")
# end_time = time.time()

# print(f"Runtime: {end_time - start_time} detik")