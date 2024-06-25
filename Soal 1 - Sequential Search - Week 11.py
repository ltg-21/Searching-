def sequential_search(arr, x):
    for item in arr:
        if item == x:
            return True
    return False

def main():
    # Data barang di masing-masing lokasi
    rumah_sakit = ['alat bedah', 'alat periksa', 'kursi roda', 'masker', 'obat', 'bankar']
    sekolah = ['buku', 'kapur', 'kursi', 'komputer', 'papan tulis', 'proyektor']
    rumah = ['bantal', 'lemari', 'kompor', 'meja', 'televisi', 'sofa']
    
    # Pilih lokasi
    lokasi = input("Anda akan mencari barang di (rumah sakit/sekolah/rumah): ").lower()
    
    # Pilih barang yang akan dicari
    barang = input("Barang yang akan anda cari adalah: ").lower()
    
    # Menentukan daftar barang berdasarkan lokasi
    if lokasi == "rumah sakit":
        barang_list = rumah_sakit
    elif lokasi == "sekolah":
        barang_list = sekolah
    elif lokasi == "rumah":
        barang_list = rumah
    else:
        print("Lokasi tidak valid!")
        return
    
    # Mencari barang menggunakan sequential search
    found = sequential_search(barang_list, barang)
    
    if found:
        print(f"Barang '{barang}' ditemukan di {lokasi}.")
    else:
        print(f"Barang '{barang}' tidak ditemukan di {lokasi}.")

if __name__ == "__main__":
    main()
