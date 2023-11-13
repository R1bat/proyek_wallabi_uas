# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 12:53:28 2023

@author: Arribaat
"""

def greeting():
    print ("----------------------------------".center(90))
    print ("SIGN UP".center(90))
    print ("----------------------------------".center(90))
    print ("")
    
def data_diri():
    print("")
    greeting()
    print("Lengkapi data diri anda!")
    nama = str(input("Masukkan Nama: "))
    umur = int(input("Masukkan Umur: "))
    alamat = str(input("Masukkan Alamat: "))
    email = input("Masukkan Alamat E-mail: ")
    no_hp = input("Masukkan No.HP: ")
    #jenis kelamin = input("Masukkan Jenis Kelamin: ") 
    #pekerjaan = input("Masukkan Pekerjaan: ")
    datadiri = [nama,umur,alamat,email,no_hp]
    return datadiri
   

def Jenis_Kelamin():
    print ("Jenis Kelamin: P/W ")
    choice = int(input("1. Pria\
                        2. Wanita\
                         "))
    print("")
    
    if choice == 1:
        print("arahin ke database preferensi pria")
    elif choice == 2:
        print("arahin ke database preferensi wanita")
    else:
        print("Invalid choice. Silahkan masukkan 1 atau 2")
        
def pekerjaan():
    print("Apa Pekerjaan Anda?")
    choice = int(input("1. Mahasiswa\
                        2. Punya penghasilan tetap\
                        3. Tidak punya penghasilan tetap\
                         "))
    print("")
    if choice == 1:
        print("arahin ke database preferensi mahasiswa")
    elif choice == 2:
        print("arahin ke database preferensi punya penghasilan tetap")
    elif choice == 3:
        print("arahin ke database preferensi tidak punya penghasilan tetap")
    else:
        print("Invalid choice. Silahkan masukkan 1, 2 atau 3")   

