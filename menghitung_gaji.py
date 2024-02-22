def hitung_total_gaji(gaji_pokok, uang_transport_perhari, uang_makan_perhari, hari_kerja, jam_lembur, hari_lembur):

    total_uang_transport = uang_transport_perhari * hari_kerja
    total_uang_makan = uang_makan_perhari * hari_kerja

    upah_lembur_per_jam_pertama = 100_000
    upah_lembur_per_jam_berikutnya = 150_000

    total_upah_lembur = (upah_lembur_per_jam_pertama * 2) + (upah_lembur_per_jam_berikutnya * (jam_lembur - 2))

    total_gaji = gaji_pokok + total_uang_transport + total_uang_makan + total_upah_lembur * hari_lembur

    return total_gaji

gaji_pokok = float(input("Masukkan gaji pokok Anda: "))
uang_transport_perhari = float(input("Masukkan uang transport perhari: "))
uang_makan_perhari = float(input("Masukkan uang makan perhari: "))
hari_kerja = int(input("Masukkan jumlah hari kerja dalam sebulan: "))
jam_lembur = int(input("Masukkan jumlah jam lembur perhari: "))
hari_lembur = int(input("Masukkan jumlah hari lembur dalam sebulan: "))

total_gaji = hitung_total_gaji(gaji_pokok, uang_transport_perhari, uang_makan_perhari, hari_kerja, jam_lembur, hari_lembur)

print("Total gaji bulanan Anda adalah:", total_gaji)
