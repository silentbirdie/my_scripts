
import mysql.connector

cnx = mysql.connector.connect(user='root', database='utilisateurs')
cursor = cnx.cursor()

with open("/etc/passwd","r") as fic_in:
    for ligne in fic_in:
        user,filler,uid,gid,gecos,home,login = ligne.rstrip().split(":")
        uid=int(uid)
        gid=int(gid)
        add_user = ("INSERT INTO users (user,filler,uid,gid,gecos,home,login) VALUES (%s, %s, %s, %s, %s, %s, %s)")
        data_user=(user,filler,uid,gid,gecos,home,login)
        cursor.execute(add_user,data_user)

cnx.commit()
cursor.close()
cnx.close()


