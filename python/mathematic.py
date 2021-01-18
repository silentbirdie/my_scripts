#!/usr/bin/env python3
def power(n,e):
    if e == 0:return(1)
    return(n*power(n,e-1))

print(power(5,3))
print(5**3)
#
#factorielle
#
# fact(n) = n*fact(n-1)
# fact(0) = 1
# fact(1) = 1
# fact(5) = 5*4*3*2*1
def fact(n):
    if n == 0 or n -- 1: return(1)
    return(n*fact(n-1))

print(fact(5))
