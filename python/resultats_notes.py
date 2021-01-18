import mysql.connector
from mysql.connector import errorcode
try:
    mydb = mysql.connector.connect(host="localhost", user="root", password="P@ssword221996", database="notes")
except mysql.connector.Error as err:
    print(f"Message d'erreur : {err}")
    quit()
mycursor = mydb.cursor()
query="SELECT avg(final) FROM examens"
try:
    mycursor.execute(query)
    myresult=mycursor.fetchall()
    if len(myresult) != 0:
        for ligne in myresult:
            print(ligne)
    else:
        print("Pas de selection pour")
        mycursor.close()
except mysql.connector.Error as err:
    print(f"Message d'erreur : {err}")
mydb.close()
