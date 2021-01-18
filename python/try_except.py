#!/usr/bin/env python3
#
while True:
	try:
		variable=input("Saisir une valeur ou CTRL/C pour terminer : ")
		print(1/int(variable))
	except ZeroDivisionError as e:
		print ("tentative de division par zéro !!!")
	except ValueError as e:
		print ("Erreur de conversion de type  !!!")
	except KeyboardInterrupt as e:
		print ("\nInterception de CTRL/C          !!!\n")
		quit()
	except Exception as e:
		print(e)

