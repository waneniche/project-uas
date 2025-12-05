python

from collections import deque

stack = deque()

while True:
    print("\n=== PROGRAM STACK ===")
    print("1. Append (Tambah belakang)")
    print("2. AppendLeft (Tambah depan)")
    print("3. Pop (Hapus belakang)")
    print("4. PopLeft (Hapus depan)")
    print("5. Clear (Hapus semua)")
    print("6. Keluar")

    menu = input("Pilih menu (1-6): ")

    if menu == '1':
        data = input("Masukkan data: ")
        stack.append(data)
        print("Data berhasil ditambahkan:", stack)

    elif menu == '2':
        data = input("Masukkan data: ")
        stack.appendleft(data)
        print("Data berhasil ditambahkan di depan:", stack)

    elif menu == '3':
        if len(stack) > 0:
            stack.pop()
            print("Data belakang berhasil dihapus:", stack)
        else:
            print("Stack kosong!")

    elif menu == '4':
        if len(stack) > 0:
            stack.popleft()
            print("Data depan berhasil dihapus:", stack)
        else:
            print("Stack kosong!")

    elif menu == '5':
        stack.clear()
        print("Semua data terhapus. Stack kosong!")

    elif menu == '6':
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")
