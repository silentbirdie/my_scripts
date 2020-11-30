#!/usr/bin/python
# -*- coding=utf-8 -*-
#entre_sortie_std.py
import sys
chaine = "introduire une chaine :"
sys.stdout.write(chaine + "\n" )
while len(chaine) != 1 :
    chaine=sys.stdin.readline()
    sys.stdout.write(chaine)
if len(chaine) == 1 :
    sys.stderr.write("Error\n")
