#!/usr/bin/env python3
#
# Script python qui interroge la base de donnée « utilisateurs » 
# Utilisation d'une requete « sql » clause « SELECT »  avec « where »
# Donne la liste des informations fournit par le service « mysqld »
#
#====================================================================
import mysql.connector
bd = mysql.connector.connect(host="localhost", user="root", password="", database="utilisateurs")
cursor = bd.cursor()
uid=int(input("UID à rechercher : "))
query = "SELECT * from users WHERE uid = %s"
cursor.execute(query % uid)
resultat = cursor.fetchall()
if len(resultat) != 0:
	for ligne in resultat:	
		print(ligne)
else:
	print("Pas de selection pour la table « users »")
cursor.close()
bd.close()

