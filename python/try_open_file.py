#!/usr/bin/env python3
#
while True:
	try:
		fichier=input("donnez un nom de fichier texte ou CTRL/C pour terminer : ")
		f=open(fichier)
	except IOError as e:
		print ("tentative d'ouverture du fichier",fichier)
	except KeyboardInterrupt as e:
		print ("\nInterception de CTRL/C          !!!\n")
		quit()
