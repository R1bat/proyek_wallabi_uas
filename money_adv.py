def RekomendasikanPenyaluranDana():
    tabungan = float(input("Masukkan jumlah tabungan yang ingin disalurkan untuk investasi: "))

    if 500000 <= tabungan <= 2000000:
        print("Investasi ke Reksadana dan Crypto")
    elif 1000000 <= tabungan <= 10000000:
        print("Investasi ke Buka Jasa Print, Pedagang Retail, Tanaman Hias, dan Laundry")
    elif 25000000 <= tabungan <= 50000000:
        print("Investasi ke Beli Sawah, Jual Beli Elektronik, Investasi Jasa Rental, Jasa Jual Beli Motor, Retail Kamera dan Fotografi, Bengkel Motor, Reksadana")
    elif 50000000 <= tabungan <= 100000000:
        print("Investasi ke Apotek, Gym, Buka Cafe, Travel, Usaha Properti, Bengkel Mobil")
    elif tabungan > 100000000:
        print("Investasi ke Jual Beli Mobil, Membuka Kost-Kostan, Developer, Rumah, Membeli Perkebunan, Investasi Rumah")
    else:
        print("Jumlah tabungan tidak mencukupi untuk investasi. Pilihan investasi:")
        print("1. Rp. 500.000 - Rp. 2.000.000")
        print("2. Rp. 1.000.000 - Rp. 10.000.000")
        print("3. Rp. 25.000.000 - Rp. 50.000.000")
        print("4. Rp. 50.000.000 - Rp. 100.000.000")
        print("5. > Rp. 100.000.000")

        # Proses selesai
