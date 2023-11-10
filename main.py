# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 13:51:35 2023

@author: Arribaat
"""

#var global = user_arr (variabel sementara user), data_user (variabel hasil konfersi dengan json), username (nama file user), client (dictionary sementara user)

import os
import json
import time
import getpass as gp

user_arr = []
#varaibel array yang akan menampung data sementara user pada sistem

def find_app_dir():
    script_dir = os.path.dirname(os.path.abspath(__name__))
    root_dir = os.path.dirname(script_dir)
    return root_dir.split()

def read_data(usr):
    path_data = find_app_dir()[0] + "\\usr_data\\" + usr + ".json"
    
    global data_user
    with open(path_data) as datauser: 
    #membuka file data
        data_user = json.load(datauser) 
        #transformasi data dari json ke dictionary
    
def add_data(usr):
    path_data = find_app_dir()[0] + "\\usr_data\\" + usr + ".json"
    with open(path_data,'x') as newfile: 
        #membuat file json baru
        json.dump(user_arr,newfile) 
        #memindahkan data client ke file json
        
def greeting(): 
    # fungsi sapaan di awal
    os.system('cls') 
    #clear screen(menghapus kode tampilan sebelumnya)
    
    stripvar = "---------------------" 
    #variabel strip
    
    print(stripvar.center(120))
    print("Selamat datang di Wallabi ".center(120))
    print("Konsultan keuangan digital".center(120))
    print(stripvar.center(120))
    print("")

def init(): 
    #fungsi tampilan sign in dan login
    print("1. Login")
    print("2. Sign Up")
    choice = int(input("Pilih menu: "))
    if choice == 1: 
    #jika memilih angka 1
        greeting()
        login()
        
    elif choice == 2: 
    #jika memilih angka 2
        greeting()
        sign_up()
        
    else:
        os.system('cls')
        print("Invalid choice!\nSilahkan masukkan 1 atau 2")
        print("")
        init()
        
def sign_up(): 
    #fungsi pendaftaran user baru
    global username
    username = input("Masukkan username: ")
    
    try:
        read_data(username)
        file_exist = True
    except:
        file_exist = False
    
    if file_exist == False :  #jika file belum ada 
        password = gp.getpass("Masukkan password: ")
        #meminta password dari user
        konfirmasi = gp.getpass("Konfirmasi password: ")
        #getspass adalah fungsi input yang disembunykian
        
        if konfirmasi == password:
        #apabila password terkonfirmasi
            greeting()
            print("Sandi cocok")
            
            time.sleep(1)
            #jeda user untuk menerima informasi bahwa sandi cocok
            os.system('cls')
            #membersihkan screen console
            
            global client
            #membuat variabel client untuk data user
            client = {}
            client["password"] = password
            
            import sign_up as su
            datadiri = su.data_diri()
            listkey = ["nama","umur","alamat","email","no_hp"]
            for key in range(len(listkey)):
               client[listkey[key]] = datadiri[key]
              
            user_arr.append(client)
            add_data(username)
                
            os.system('cls')
            init() #kembali ke laman utama
            
        else:
            greeting()
            print("Sandi tidak cocok")
            sign_up
            
    elif file_exist == True: #jika file sudah ada
        greeting()
        print("Maaf username sudah digunakan, masukkan username unik")
        print("")
        sign_up()

def login(): #fungsi login
    
    username = input("Masukkan username: ")
    try:
        read_data(username)
        file_exist = True
    
    except:
        file_exist = False
    
    if file_exist == True :  #jika file sudah ada 
        password = gp.getpass("Masukkan password: ")
        if password == data_user[0]["password"] : 
        #jika password sama dengan password user dalam dict json
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
