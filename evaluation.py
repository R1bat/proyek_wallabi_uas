#nanti import fungsi rekomendasi pekerjaan dan penyaluran dana

def evluasi_keuangan():
    #input mau di dalam atau di luar fungsi? kalau dji luar fungsi bisa pake parameter, 
    # tapi klu bingung sementara di dalam aja dulu
    tabungan=int(input('Masukkan nominal tabungan anda saat ini : Rp.'))
    penghasilan=int(input('Masukkan nominal penghasilan anda saat ini : Rp.'))
    pengeluaran=int(input('Masukkan nominal pengeluaran anda saat ini : Rp.'))

    if pengeluaran > penghasilan :
        print("Pengeluaran Anda melebihi pemasukan yang direncanakan.")
        print("Evaluasi sifat") #->sifat kita bahas senin
        tabungan -= pengeluaran-penghasilan
        #REKOMENDASI_PEKERJAAN() ->kalau sudah di import baru di pake

    elif pengeluaran < penghasilan:
        print("Apresiasi") #->kita pikirin senin
        tabungan += penghasilan - pengeluaran
        #PENYALURAN_DANA()


