ulang = 2

for i in range(ulang):
    print("Data Ke - " + str(i+1))
    nama = input("Masukkan NIM anda : ")
    uts = int(input("Masukkan Nilai UTS anda : "))
    uas = int(input("Masukkan Nilai UAS : "))
    print("Nim anda adalah %s nilai UTS anda %i nilai UAS anda %i" % (nama, uts, uas))
    print("-------------------------------------\n")