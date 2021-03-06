#!/usr/bin/env python3
#
# Script python qui interroge la base de donnée « utilisateurs » 
# Utilisation d'une requete « sql » clause « SELECT » 
# Donne la liste des informations fournit par « mysql » sous forme de table formattée
# avec le module « prettytable »
#
#====================================================================================
import mysql.connector
from prettytable import PrettyTable

bd = mysql.connector.connect(host="localhost", user="root", password="", database="utilisateurs")
cursor = bd.cursor()
query=("SELECT * FROM users")
cursor.execute(query)
resultat = cursor.fetchall()
x = PrettyTable()
x.field_names = ["User","Filler","Uid","Gid","Gecos","Home","Login"]
x.align["User"]  = "l"
x.align["Gecos"] = "l"
x.align["Home"]  = "l"
x.align["Login"] = "l"
x.align["Uid"]   = "r"
x.align["Gid"]   = "r"
x.add_rows(resultat) 
print(x)
cursor.close()
bd.close()

