# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:55:29 2023

@author: Arribaat
"""
import os
import getpass
import json

#var penyimpanan data user sementara
stripvar = "---------------------" #variabel strip

def greeting(): #sapaan di awal
    os.system('cls') #clear screen(menghapus kode tampilan sebelumnya)
    print(stripvar*4)
    print("Selamat datang di Wallabi ".center(90))
    print("Konsultan keuangan digital".center(90))
    print(stripvar*4)
    print("")

def init(): #Tampilan sign in dan login
    print("1. Login")
    print("2. Sign Up")
    choice = int(input("Pilih menu: "))
    if choice == 1: #jika memilih angka 1
        greeting()
        login()
        
    elif choice == 2: #jika memilih angka 2
        greeting()
        sign_up()
        
    else:
        print("Invalid choice.\nSilahkan masukkan 1 atau 2")
        
def sign_up(): #fungsi masuk
    client = {"password":""}
    username = input("Masukkan username: ")
    file_path=username + ".json"
    if not os.path.exists(file_path):
        password = getpass.getpass("Masukkan password: ") #getspass untuk mentransparankan pass yg dimasukkan
        konfirmasi = getpass.getpass("Konfirmasi password: ")
        with open(username + ".json") as datauser: #untuk menentukan apakah file sudah ada atau tidak
            data_user = json.load(datauser) #mengambil data dari json ke dictionary
        file_exist = True
        if konfirmasi == password:
            greeting()
            print("Sandi cocok")
            client["password"] = password
            
            with open(username + ".json",'x') as file: #membuat file json baru
                json.dump(client,file) #memindahkan data client ke file json
            
            init() #kembali ke laman utama
                
        else: #jika konfirmasi tidak sama dengan password
            greeting()
            print("Sandi tidak cocok")
            sign_up
    else:
        greeting()
        print("Maaf username sudah digunakan, masukkan username unik")
        print("")
        sign_up()

def login(): #fungsi login
    
    username = input("Masukkan username: ")
    
    try : 
        with open(username + ".json") as datauser: #untuk menentukan apakah file sudah ada atau tidak
            data_user = json.load(datauser) #mengambil data dari json ke dictionary
        file_exist = True
    except:
        file_exist =  False
    
    if file_exist == True :  #jika file sudah ada 
        password = getpass.getpass("Masukkan password: ")
        if password == data_user["password"] : #jika password sama dengan password user dalam dict json
            print("Login Berhasil!")
            
        else :
            greeting()
            print("Login Gagal, mohon ingat password anda")
            print("")
            init()
            
    elif file_exist == False:
        greeting()
        print("Username Tidak Ditemukan")
        print("")
        init()

greeting()        
init()

#write data di akhir program ketika program berhenti
#selama program masih berjalan, maka data akan disimpan variabel di dalam terminal
