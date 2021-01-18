#!/usr/bin/env python3
#
# Importer le module « connector »
import mysql.connector

# Importer la classe qui gère les erreurs
from mysql.connector import errorcode

# Connexion à la base de données « mysql » ( prédéfinie ) 
try:
  cnx = mysql.connector.connect(user='root', password='P@ssword221996',host='localhost',database='mysql')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
  	print("Il y a un problème avec votre nom d'utilisateur ou votre mot de passe")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("La base de données n'existe pas")
  else:
    print(err)
else:
  cnx.close()
