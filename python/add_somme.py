#!/usr/bin/env python3
#
# Script qui additionne 2 nombres passes comme arguments
#
import sys
#
#la propriete argv , qui est une liste des argument : sys.argv ( sys.argv[0] : nom du script ) 
#
# verifier s'il y  2 arguments ( en plus du nom du script)
#verification de la syntaxe du script
#
#
if len(sys.argv) < 2 :
    print("Syntaxe : ",sys.argv[0] , "arg1 ...argn")
    sys.exit(1)

#
#il y as 2 aperandes , on fait l'addition ( op1 + op2 )
del(sys.argv[0])
somme=0
for op in sys.argv :
    somme += float(op)
print("somme = " , somme )
