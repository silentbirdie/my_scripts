#!/usr/bin/env python3
#
# Test simple de connexion au serveur mysql à la base de données prédéfinie « mysql »
# Ce script simple gère les erreurs de connexion
#
# Importation du module « mysql.connector »
import mysql.connector
#
# Importation de la classe des erreurs « errorcode » du module « mysql.connector »
from mysql.connector import errorcode

user     = "root"
database = "utilisateurs"

try:
  cnx = mysql.connector.connect(user=user,database=database)
  print(f"Connexion à la base « {database} » réussie ")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print(f"Code erreur : {errorcode.ER_ACCESS_DENIED_ERROR}")
    print("Il y a un problème avec votre nom d'utilisateur ou votre mot de passe")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print(f"Code erreur : {errorcode.ER_BAD_DB_ERROR}")
    print(f"La base de données « {database} » n'est pas accéssible ou n'existe pas")
  elif err.errno == errorcode.CR_CONN_HOST_ERROR :
    print(f"Code erreur : {errorcode.CR_CONN_HOST_ERROR}")
    print("Verifier si service MYSQL est démarre")
  else:  
    print(f"Message d'erreur : {err}")
else:
  cnx.close()

