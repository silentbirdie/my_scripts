#!/usr/bin/env python3
def power(n,e):
    if e == 0:return(1)
    return(n*power(n,e-1))

print(power(5,3))
print(5**3)
