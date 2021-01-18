#!/usr/bin/env python3
import mysql.connector
cnx = mysql.connector.connect(user='root',password='P@ssword221996',database='notes')
cursor = cnx.cursor()
with open("/home/chris/notes.txt","r") as fic_in:
    for ligne in fic_in:
        etudiant,intra,final,tp01,tp02 = ligne.rstrip().split(":")
        intra = float(intra)
        final = float(final)
        tp01 = float(tp01)
        tp02 = float(tp02)
        add_user = ("INSERT INTO examens (etudiant,intra,final,tp01,tp02) VALUES (%s, %s, %s, %s, %s)")
        data_user=(etudiant,intra,final,tp01,tp02)
        cursor.execute(add_user,data_user)
cnx.commit()
cursor.close()
cnx.close()
