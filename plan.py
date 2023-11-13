# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 13:53:03 2023

@author: Arribaat
"""

def tambah_kegiatan(kegiatan, kategori, jumlah_pengeluaran):
    daftar_kegiatan.append(kegiatan)
    daftar_kategori.append(kategori)
    daftar_pengeluaran.append(jumlah_pengeluaran)
    print("Kegiatan berhasil ditambahkan!")

def tampilkan_kegiatan():
    if len(daftar_kegiatan) == 0:
        print("Tidak ada kegiatan dalam daftar.")
    else:
        for i in range(len(daftar_kegiatan)):
            print(f"{i+1}. {daftar_kegiatan[i]} - Kategori: {daftar_kategori[i]} - Jumlah Pengeluaran: ${daftar_pengeluaran[i]}")

def hapus_kegiatan(index):
    if index >= 0 and index < len(daftar_kegiatan):
        del daftar_kegiatan[index]
        del daftar_kategori[index]
        del daftar_pengeluaran[index]
        print("Kegiatan berhasil dihapus!")
    else:
        print("Indeks kegiatan tidak valid.")


daftar_kegiatan = []
daftar_kategori = []
daftar_pengeluaran = []

def menu_plan():
    while True:
        print("\n===== PLAN KEUANGAN =====")
        print("1. Tambah Kegiatan")
        print("2. Tampilkan Kegiatan")
        print("3. Hapus Kegiatan")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan (1/2/3/4): ")

        if pilihan == "1":
            kegiatan = input("Masukkan nama kegiatan: ")
            kategori = input("Masukkan kategori kegiatan: ")
            jumlah_pengeluaran = float(input("Masukkan jumlah pengeluaran untuk kegiatan ini: $"))
            tambah_kegiatan(kegiatan, kategori, jumlah_pengeluaran)
        elif pilihan == "2":
            tampilkan_kegiatan()
        elif pilihan == "3":
            index = int(input("Masukkan indeks kegiatan yang ingin dihapus: "))
            hapus_kegiatan(index-1)
        elif pilihan == "4":
            print("Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")
        