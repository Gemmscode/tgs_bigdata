import csv

# Fungsi mapper untuk memproses satu kolom
def mapper(namafile):
    with open(namafile, 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file)
        mapped_values = []
        for row in reader:
            try:
                # Ambil Nilai dari satu-satunya kolom yang ada
                Nilai = float(list(row.values())[0])
                mapped_values.append(Nilai)
            except ValueError:
                continue 
    return mapped_values

# Fungsi menghitung frekuensi Nilai 80 dan 90
def count_specific_values_no_if(values, specific_values):
    return {value: len(list(filter(lambda x: x == value, values))) for value in specific_values}

def main():
    # Panggil mapper untuk membaca file CSV
    mapped_values = mapper('D:/Tugas Kuliah/dataset_nilai.csv') or exit("Tidak ada data yang bisa diproses.")
    
    # Daftar Nilai yang ingin dihitung frekuensinya (40 dan 60)
    specific_values = [40, 60]
    
    # Menghitung frekuensi Nilai 80 dan 90
    specific_value_freq = count_specific_values_no_if(mapped_values, specific_values)
    
    # Menampilkan hasil perhitungan frekuensi
    print("Frekuensi Nilai 40 dan 60:")
    for Nilai, frekuensi in specific_value_freq.items():
        print(f"Nilai: {Nilai}, Frekuensi: {frekuensi}")

if __name__ == "__main__":
    main()