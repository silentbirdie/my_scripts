import mysql.connector
from mysql.connector import errorcode
try:
    mydb = mysql.connector.connect(host="localhost", user="root", password="P@ssword221996", database="utilisateurs")
except mysql.connector.Error as err:
    print(f"Message d'erreur : {err}")
    quit()

mycursor = mydb.cursor()
uid=int(input("Votre uid : "))
query="SELECT * FROM users WHERE uid = {}".format(uid)

try:
    mycursor.execute(query)
    myresult=mycursor.fetchall()
    if len(myresult) != 0:
        for ligne in myresult:
            print(ligne)
    else:
        print("Pas de selection pour uid = {}".format(uid))
except mysql.connector.Error as err:
    print(f"Message d'erreur : {err}")
mycursor.close()
mydb.close()
