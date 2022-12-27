import hashlib
import getpass
import mysql.connector

cnx = mysql.connector.connect(user='kullanici_adi', password='sifre', host='localhost', database='veritabani_adi')
cursor = cnx.cursor()

def displayMenu():
    status = input("Zaten Kayitli Misin y/n? Press q to quit: ")
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()

def newUser():
    createLogin = input("Kullanici Adi Olustur: ")
    createPassw = getpass.getpass(prompt="Sifre Olustur: ")
    hashed_password = hashlib.sha256(createPassw.encode()).hexdigest()

    add_user = "INSERT INTO users (username, password) VALUES (%s, %s)"
    user_data = (createLogin, hashed_password)
    cursor.execute(add_user, user_data)
    cnx.commit()

    print("\nUser created\n")

def oldUser():
    login = input("Kullanici ismin: ")
    passw = getpass.getpass(prompt="Sifren: ")
    hashed_password = hashlib.sha256(passw.encode()).hexdigest()

    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    cursor.execute(query, (login, hashed_password))
    result = cursor.fetchone()

    if result:
        print("\nLogin successful!\n")
    else:
        print("\nSifre Yanlis Veyahut Hesap Yok!\n")

while status != "q":
    displayMenu()

cursor.close()
cnx.close()
