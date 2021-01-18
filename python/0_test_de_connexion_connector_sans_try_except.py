#!/usr/bin/env python3
#
# Test simple de connexion au serveur mysql à la base de données prédéfinie « mysql »
# Ce script simple ne gère pas les erreurs de connexion
#
# Importation du module « mysql.connector »
import mysql.connector
# Connexion à serveur ( service ) « mysqld » , à la base de données  mysql » local « localhost » qu'on peut remplacer par l'adresse « ip » 
cnx = mysql.connector.connect(user='root',password='',host='localhost',database='mysql')
# Fermeture de la connexion
cnx.close()
