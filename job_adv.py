def RekomendasiPekerjaan():
    hobi = input("Masukkan Hobi: ")
    print("Berikut adalah pilihan kesibukan : ")
    print("1. Pelajar atau Mahasiswa")
    print("2. Pekerja Tetap")
    print("3. Pengangguran")
    kesibukan = int(input(" Silahkan masukkan salah satu angka di atas : "))

    if kesibukan == 1:
        if hobi == "Suka Membaca":
            print(" Anda dapat mencoba pekerjaan sebagai Editor, Responden")

        elif hobi == "Menulis":
            print("Anda dapat mencoba pekerjaan sebagai Content Writer")

        elif hobi == "Seni Dan Ilustrasi":
            print("Anda dapat mencoba pekerjaan sebagai Content Creator")

        elif hobi == "Memasak":
            print("Anda dapat mencoba pekerjaan sebagai Usaha Makanan Ringan, Asisten Chef")

        elif hobi == "Mengajar":
            print("Anda dapat mencoba pekerjaan sebagai Tutor")

        elif hobi == "Punya Kendaraan":
            print("Anda dapat mencoba pekerjaan sebagai Ojol")
    elif kesibukan == 2 :
        print("Anda dapat mencoba bekerja sebagai : Konsulltan, tutor/narasumber, \n dan trainer dengan materi yang sesuai dengan ilmu dan pekerjaan Anda. \n Selain itu, jika Anda cakap berteknologi Anda dapat menjadi asisten Virtual dengan mendaftar diri di web freelence yang ada \n salah satunya sribulencer. Jika anda memiliki kendaraan Anda dapat memiliki pekerjaan sampingan sebagai ojek online")
                #perbaiki lagi
    elif kesibukan==3 : 
        pendidikan_terakhir = input("Masukkan Pendidikan Terakhir (SD/SMP/SMA/SMK): ")

        if pendidikan_terakhir == "SD":
            pekerjaan_SD = [
            "Pekerjaan yang bisa dilakukan:",
            "A. Kuli Bangunan",
            "B. Petugas Kebersihan",
            "C. Sopir",
            "D. Pramusaji",
            "E. Tukang Kebun"]
            print("pekerjaan_SD")

        elif pendidikan_terakhir == "SMP":
            pekerjaan_SMP = [
            "Pekerjaan yang bisa dilakukan:",
            "A. Beternak Dan Bertani Modern",
            "B. Satpam",
            "C. Sopir",
            "D. Gabung Lsm",
            "E. Pramusaji",
            "F. Waiter"]
            print(pekerjaan_SMP)

        elif pendidikan_terakhir == "SMA":
            pekerjaan_SMA = [
            "Pekerjaan yang bisa dilakukan:",
            "A. Tutor Les",
            "B. Pengasuh Anak",
            "C. Pramu Wisma",
            "D. Kasir",
            "E. Admin Sederhana",
            "F. Event Organiser",
            "G. Tempat Gym",
            "H. Pengisi Suara",
            "I. Cpns"]
            print(pekerjaan_SMA)

        elif pendidikan_terakhir == "SMK":
            pekerjaan_SMK = [
            "Pekerjaan yang bisa dilakukan:",
            "Bidang Kecantikan:",
            "A. Karyawan Salon",
            "B. MUA",
            "Bidang Tata Busana:",
            "A. Menjahit",
            "B. Desainer Pakaian",
            "Tata Boga:",
            "A. Koki",
            "B. Usaha Kue Dan Makanan",
            "C. Rumah Makan",
            "Bidang Teknik:",
            "A. Usaha Bengkel",
            "B. Servis Elektronika",
            "C. Jasa Instalasi",
            "D. Perancangan Jaringan Atau Bangunan",
            "E. Percetakan",
            "F. Toko Alat Alat Teknik",
            "G. Dan Selebihnya Menyesuaikan"
            ] #pekerjaan ini menurutku belum fix, rencananya mau jadi tipe data dict yg valuenya itu penjelasan
            #ini biar punya kita jalan dulu aja, senin pikirin isinya

        #elsenya masih ragu   
            # tambahkan skill? 
    else : 
        print("Data yang Anda masukkan belum lengkap ") 

    #tambahin cara kembali ke menu utama atau keluarnya ya makasii