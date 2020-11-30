#!/usr/bin/env python3
#
#lire et afficher le contenu du fichiers /etc/passwd
#
# 1- ouverture du fichiers
#
fic_in = open ("/etc/passwd","r")
#
# 2 - acces aux donnees du fichiers
#
#
# lire le fichiers globalement
#
print(fic_in.readlines())
print( "=" * 30)
#
#3 - fermer le fichiers ( methode close())
#
fic_in.close()
#
# Methode 2 lire le fichier ligne par ligne
#
for ligne in open("/etc/passwd","r"):
    print(ligne.rstrip()) # methode rstrip() : supprimer le saut de ligne
fic_in.close()
#
#
#

for ligne in open("/etc/passwd","r"):
    print(ligne.rstrip()) # methode rstrip() : supprimer le saut de ligne    
#
#lire l
#
#methode 3 avec la clause "with"
#
with open("/etc/passwd","r") as fic_in:
    for ligne in fic_in:
        print(ligne.rstrip()) #methode rstrip() : supprimer suat de ligne
#
# method
#
with open("/etc/passwd","r") as fic_in:
    print(fic_in.read(4))
