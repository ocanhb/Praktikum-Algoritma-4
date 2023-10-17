hari_bulan = {
    1: 31,  # Januari
    2: 28,  # Februari
    3: 31,  # Maret
    4: 30,  # April
    5: 31,  # Mei
    6: 30,  # Juni
    7: 31,  # Juli
    8: 31,  # Agustus
    9: 30,  # September
    10: 31,  # Oktober
    11: 30,  # November
    12: 31   # Desember
}

while True:
    bulan = int(input("Masukkan angka bulan (1-12) untuk menjalankan program, dan ketik -1 untuk mengakhiri program: "))

    if bulan == -1:
        print("Terima kasih telah menggunakan program ini, sampai jumpa kembali")
        break

    if bulan < 1 or bulan > 12:
        print("Bulan yang dimasukkan tidak valid.")
    else:
        tahun = int(input("Masukkan tahun (YYYY): "))

        if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
            hari_bulan[2] = 29
        else:
            hari_bulan[2] = 28

        jumlah_hari = hari_bulan[bulan]
        print(f"Jumlah hari dalam bulan {bulan} tahun {tahun} adalah {jumlah_hari} hari.")
