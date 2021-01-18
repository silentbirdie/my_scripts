#!/usr/bin/env python3
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="P@ssword221996", database="utilisateurs")
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM users where uid = 0")
myresult = mycursor.fetchall()

for line in myresult:
    print(line)

#print(myresult)
#print(myresult[0])
mycursor.close()
mydb.close()
     
