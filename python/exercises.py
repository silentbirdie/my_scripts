#!/usr/bin/env python3
import os
os.system("clear")
tracer="=" * 20
#avec une boucle, affichez les noombres 1 a 10 sur une seule ligne
for i in range(1,11):
    print(i,end=" ")
print("")
print(tracer)
#soit << impairs >> la liste impaires [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21].
impaires = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
paires=[ i+1 for i in impaires]
print(paires)
print(tracer)
paires=[]
#print(paires)
for i in impaires:paires+=[i+1]
print(paires)
#
notes=[70, 45, 30, 40, 60]
moyenne=sum(notes)/len(notes)
print("moyenne = {:7.2f}".format(moyenne))
