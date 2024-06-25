def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        mid_value = arr[mid][1]  # Mengambil nilai dari tuple (nama, nilai)

        if mid_value == target:
            return mid
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Contoh penggunaan
if __name__ == "__main__":
    # Daftar mahasiswa dan nilai mereka (nama, nilai)
    mahasiswa = [
        ("Alexander", 55), 
        ("Bryan", 60), 
        ("Cynthia", 65), 
        ("Damian", 70), 
        ("Eleanor", 75), 
        ("Felix", 80), 
        ("Gevon", 85), 
        ("Hades", 90), 
        ("Irene", 95), 
        ("Jaeden", 100)
    ]

    # Urutkan daftar mahasiswa berdasarkan nilai
    mahasiswa.sort(key=lambda x: x[1])

    # Meminta pengguna untuk memasukkan nilai yang ingin dicari
    target_nilai = int(input("Masukkan nilai mahasiswa yang ingin dicari: "))

    # Mencari nilai menggunakan binary search
    hasil = binary_search(mahasiswa, target_nilai)

    if hasil != -1:
        nama_mahasiswa = mahasiswa[hasil][0]
        print(f"Nilai {target_nilai} ditemukan, nama mahasiswa: {nama_mahasiswa}")
    else:
        print(f"Nilai {target_nilai} tidak ditemukan dalam daftar")
