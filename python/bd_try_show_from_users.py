#!/usr/bin/env python3
import mysql.connector
try:
mydb = mysql.connector.connect(host="localhost", user="root", password="", database="utilisateurs")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM users")
myresult = mycursor.fetchall()
print(type(myresult))
print(type(myresult[0]))
mycursor.close()
mydb.close()
except:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:                               
        print("Il y a un problème avec votre nom d'utilisateur ou votre mot de passe")      
