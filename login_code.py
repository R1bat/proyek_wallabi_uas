# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:55:29 2023

@author: Arribaat
"""

import getpass
import json

def greeting():
    print("-------------------------".center(110))
    print("Selamat datang di Wallabi ".center(110))
    print("Konsultan keuangan digital".center(110))
    print("-------------------------".center(110))
    print("")
    
greeting()

def sign_up():
    client = {"username":"",
              "password":""}
    username = input("Masukkan username: ")
    password = getpass.getpass("Masukkan password: ")
    konfirmasi = getpass.getpass("Konfirmasi password: ")
    if konfirmasi == password:
        print("Sandi cocok")
        client["username"] = username
        client["password"] = password
        
        with open("data_user.json",'w') as file:
            json.dump(client,file)
            
    else:
        print("Sandi tidak cocok")

def login():
    username = input("Masukkan username: ")
    password = getpass.getpass("Masukkan password: ")
    
    with open("data_user.json") as datauser:
        data_user = json.load(datauser)
    #if username dan password ono neng db:
        #print("login berhasil")
    #else:
        #print("login gagal")
    if username == data_user["username"] :
        if password == data_user["password"] :
            print("Login Berhasil!")
            
        else :
            print("Login Gagal, mohon ingat password anda")
    else :
        print("Username Tidak Ditemukan","\n mohon sign up terlebih dahulu")
        
while True:
    print("1. Login")
    print("2. Sign Up")
    choice = int(input("Pilih menu: "))
    if choice == 1:
        login()
        break
    elif choice == 2:
        sign_up()
        break
    else:
        print("Invalid choice. Silahkan masukkan 1 atau 2")