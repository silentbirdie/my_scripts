#!/usr/bin/env python3
#
# 
# Ce script permet de mettre à jour un enregistrement avec la clause « update »
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
        quit()
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(f"Code erreur : {errorcode.ER_BAD_DB_ERROR}")
        print(f"La base de données « {database} » n'est pas accéssible ou n'existe pas")
        quit()
    elif err.errno == errorcode.CR_CONN_HOST_ERROR :
        print(f"Code erreur : {errorcode.CR_CONN_HOST_ERROR}")
        print("Verifier si service MYSQL est démarre")
        quit()
    else:  
        print(f"Message d'erreur : {err}")
        quit()

try :
    cursor = cnx.cursor()
    sql = "Update users set gecos = %s where uid >= %s " 
    # Exécution de la requete
    cursor.execute(sql, ("Usager Simple old",1000) )
    cnx.commit()
    print(cursor.rowcount, " record(s) modifiés ")         
except mysql.connector.Error as err:
    print(f"Message d'erreur : {err}")
    cnx.close()
    quit()
cursor.close()
cnx.close()


