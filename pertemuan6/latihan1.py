print("GEROBAK FRIED CHICKEN")
print("------------------------")
print("Kode JenisPotong Harga")
print("------------------------")
print("{:<5}{:^5}{:>10}".format('D','Dada','Rp. 2500'))
print("{:<5}{:^5}{:>10}".format('P','Paha','Rp. 2000'))
print("{:<5}{:^5}{:>10}".format('S','Sayap','Rp. 1500'))
print("------------------------")

bnk = int(input("Banyak Jenis : "))
total = 0

for i in range(bnk):
    kode = input("Kode Potong [D/P/S] : ").lower()
    pot = int(input("Banyak Potong : "))
    
    if kode == "d":
        nama = "Dada"
        harga = 2500
    elif kode == "p":
        nama = "Paha"
        harga = 2000
    elif kode == "s":
        nama = "Sayap"
        harga = 1500
    else :
        nama = "tidak ada"
        harga = 0
        
    jumlah = (harga * pot)
    total += jumlah
    
    print("Jenis ke : " +str(i+1))
    print("Jenis potong : ", nama)
    print("Jumlah Potong : ", pot)
    print("Harga Satuan : Rp", harga)
    print("Jumlah bayar : Rp",jumlah)
    print("------------------------")
    
pajak = (10 / 100) * total
totalB = total + pajak    

print("===== TOTAL PEMBAYARAN =====")
print("Jumlah Bayar : Rp", total)
print("Pajak 10% : Rp",+int (pajak))
print("Total Bayar : Rp",+int (totalB))
print("============================")