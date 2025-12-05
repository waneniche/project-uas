quicksort_descending.py
def quicksort_desc(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    kiri = [x for x in arr[1:] if x > pivot]
    kanan = [x for x in arr[1:] if x <= pivot]
    return quicksort_desc(kiri) + [pivot] + quicksort_desc(kanan)

data = [12, 45, 5, 67, 32, 66, 78, 10, 17, 9]

print("Data sebelum diurutkan:", data)
hasil = quicksort_desc(data)
print("Data setelah diurutkan (besar ke kecil):", hasil)
