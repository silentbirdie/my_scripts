#!/usr/bin/env python3
#
# Importer le module « connector »
import mysql.connector
#
# Connexion à la base de données « mysql » ( prédéfinie ) 
cnx = mysql.connector.connect(user='root', password='P@ssword221996',host='localhost',database='mysql')
cnx.close()
