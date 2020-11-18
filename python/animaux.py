#!/usr/bin/env python3
liste_animaux=input("votre liste d'animaux , separes par point-virgule << ; >> : \n")
animaux = liste_animaux.split(";")
print ("liste des animaux")
for animal in animaux:
    print (animal)
print("Est que girafe est dans la liste")
if 'girafe' in animaux:
    print("girafe existe")
else:
    print("girafe n'existe pas dans la liste")
