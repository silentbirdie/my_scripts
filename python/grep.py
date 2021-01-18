#!/usr/bin/env python3
# Script qui simule grep
import re
import sys
if len(sys.argv) !=3 :
    print("Syntaxe : " + sys.argv[0] + " motif fichier ")
    sys.exit()

motif=sys.argv[1]
fichier=sys.argv[2]

if not os.path.isfile(fichier):
    print(" n' existe pas ou n 'est un fichier ordinaire ")
    sys.exit()

fic=open(" /etc/passwd")
for l in fic:
    if re.search("^root",l):
        print(l.rstrip())
fic.close()
