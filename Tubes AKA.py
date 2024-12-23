import time
import random

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Fungsi untuk mengukur waktu eksekusi
def measure_time(sort_function, arr):
    start_time = time.perf_counter()  # Mulai pengukuran waktu
    sort_function(arr)
    end_time = time.perf_counter()  # Akhir pengukuran waktu
    return end_time - start_time

# Ukuran input yang berbeda
input_sizes = [100, 200, 300, 400, 500]
selection_sort_times = []
insertion_sort_times = []

for size in input_sizes:
    # Menghasilkan array acak
    random_array = [random.randint(1, 1000) for _ in range(size)]
    
    # Mengukur waktu eksekusi Selection Sort
    selection_time = measure_time(selection_sort, random_array.copy())
    selection_sort_times.append(selection_time)

    # Mengukur waktu eksekusi Insertion Sort
    insertion_time = measure_time(insertion_sort, random_array.copy())
    insertion_sort_times.append(insertion_time)

# Menampilkan hasil
print("Ukuran Input | Waktu Eksekusi (Selection Sort) | Waktu Eksekusi (Insertion Sort)")
for i in range(len(input_sizes)):
    print(f"{input_sizes[i]:<13} | {selection_sort_times[i]:<38} | {insertion_sort_times[i]:<38}") 