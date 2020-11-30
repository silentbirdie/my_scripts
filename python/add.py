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
if len(sys.argv) != 3:
    print("Syntaxe : ",sys.argv[0] , "arg1  arg2")
    sys.exit()

    #
#il y as 2 aperandes , on fait l'addition ( op1 + op2 )
somme=0
for op in range(1,len(sys.argv)-1) :
    somme += float(sys.argv[op])
print(op1 , "+" , op2  , " = " , op1+op2)
