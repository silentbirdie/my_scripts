#!/usr/bin/env python3
#
# passage d'arguments
#
import sys
for param in sys.argv:
    print(param)

print("Nom du script  python : " , sys.argv[0])
if len(sys.argv) > 1 :
    print("Premier argument : " , sys.argv[1])
