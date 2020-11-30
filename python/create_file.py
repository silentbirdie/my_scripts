#!/usr/bin/env python3
#
# exemple de creation d'un fichiers
#
compte="mike:maassen:administrator:network:qwerty"
fic_out=open("comptes.txt","a")
for i in range(5):
    fic_out.write(compte+"\n")
fic_out.close()
fic_in=open("comptes.txt")
print (fic_in.readlines())
fic_in.close()
