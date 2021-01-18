#!/usr/bin/env python3
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="P@ssword221996", database="utilisateurs")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM users")
myresult = mycursor.fetchall()
print(type(myresult))
print(type(myresult[0]))
mycursor.close()
mydb.close()
