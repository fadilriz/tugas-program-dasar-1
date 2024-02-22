def hitung_umur (tahun_lahir) :
    tahun_sekarang = 2024
    umur = tahun_sekarang - tahun_lahir
    return umur
    
tahun_lahir = int(input("Masukan tahun kelahiran anda : "))
umur = hitung_umur (tahun_lahir)
print("Ummur anda adalah :", umur, "tahun")