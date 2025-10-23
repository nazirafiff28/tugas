# Program Penggajian PT. DINGIN DAMAI

# Gaji pokok
gaji_pokok = 300000

# Input data karyawan
nama = input("Masukkan nama karyawan        : ")
golongan = int(input("Masukkan golongan (1/2/3)    : "))
pendidikan = input("Masukkan pendidikan (SMA/D1/D3/S1): ")
jam_kerja = int(input("Masukkan jumlah jam kerja    : "))

# --- Hitung Tunjangan Jabatan ---
if golongan == 1:
    tunjangan_jabatan = 0.05 * gaji_pokok
elif golongan == 2:
    tunjangan_jabatan = 0.10 * gaji_pokok
elif golongan == 3:
    tunjangan_jabatan = 0.15 * gaji_pokok
else:
    tunjangan_jabatan = 0

# --- Hitung Tunjangan Pendidikan ---
if pendidikan.upper() == "SMA":
    tunjangan_pendidikan = 0.025 * gaji_pokok
elif pendidikan.upper() == "D1":
    tunjangan_pendidikan = 0.05 * gaji_pokok
elif pendidikan.upper() == "D3":
    tunjangan_pendidikan = 0.20 * gaji_pokok
elif pendidikan.upper() == "S1":
    tunjangan_pendidikan = 0.30 * gaji_pokok
else:
    tunjangan_pendidikan = 0

# --- Hitung Honor Lembur ---
if jam_kerja > 8:
    lembur = (jam_kerja - 8) * 3500
else:
    lembur = 0

# --- Total Gaji ---
total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + lembur

# --- Output ---
print("\n=== SLIP GAJI KARYAWAN ===")
print("Nama Karyawan        :", nama)
print("Golongan             :", golongan)
print("Pendidikan           :", pendidikan.upper())
print("Jam Kerja            :", jam_kerja)
print("Gaji Pokok           : Rp", gaji_pokok)
print("Tunjangan Jabatan    : Rp", int(tunjangan_jabatan))
print("Tunjangan Pendidikan : Rp", int(tunjangan_pendidikan))
print("Honor Lembur         : Rp", int(lembur))
print("-------------------------------")
print("Total Gaji           : Rp", int(total_gaji))
