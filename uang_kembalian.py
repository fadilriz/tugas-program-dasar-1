def hitung_kembalian (beli_makan) :
    uang_saya = 50
    kembalian = uang_saya - beli_makan
    return kembalian

beli_makan = int(input("Masukan harga beli makan : "))
kembalian = hitung_kembalian (beli_makan) 
print("Kembaliannya adalah : " , kembalian)