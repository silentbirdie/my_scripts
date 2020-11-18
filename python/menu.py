#!/usr/bin/env python3
menu=["1 - option 1" , "2 - option 2" , "3 - option 3" , "4 - quitter"]
for m in menu:print(m)
base = int(input("votre choix? "))
if base == 1:
    print("choix 1")
elif base == 2:
    print("choix 2")
elif base == 3:
    print("choix 3")

elif base == 4:
    quit()
else:
    print ("mauvais choix")
