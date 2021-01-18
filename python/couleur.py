#!/usr/bin/env python3
color=[0,1,2,3,4,5,6,7]
acolor="\033[3"
for c in color:
    print(acolor+str(c)+"m" + "Bonjour")
