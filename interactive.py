# fungsi register to Interactive English
def daftar(nama, tgl , gender , school, parent, religion, address):
    if gender=="Perempuan":
        print("Selamat Datang di IE Nona "+nama +" Biodata kamu adalah sebagai berikut")
    print("Nama             : "+nama)
    print("Tanggal lahir    : "+tgl)
    print("Jenis Kelamin    : "+gender)
    print("Asal Sekolah     : "+school)
    print("Orang Tua        : "+parent)
    print("Agama            : "+religion)
    print("Alamat           : "+address)
    
daftar("cantika","5 agustus 2006", "Perempuan","UNPAD" , "Wiyono", "Islam", "Korea")

#absen
def absensi(nama, tanggal):
    print("Nama             : "+nama)
    print("Tanggal          : "+tanggal)
absensi("cantika", "05")

#upgrade level
def upgradelevel(nama, score, lastlevel, nextlevel):
    print("Nama             : "+nama)
    print("Score            : "+score)
    print("lastlevel        : "+lastlevel)
    print("nextlevel        : "+nextlevel)
upgradelevel("cantika","100","2","3")

#invoice spp
def invoicespp (nama, level):
    print("Nama             : "+nama)
    print("level            : "+level)
invoicespp ("cantika","3")

#check spp
def checkspp (nama):
    print("Nama             : "+nama)
checkspp("cantika")