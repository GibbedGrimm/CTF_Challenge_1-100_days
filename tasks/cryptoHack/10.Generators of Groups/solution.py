from sympy import *
import math
m = 28151
p1 = (m-1)//2
p2 = (m-1)//5
p3 = (m-1)//563
p4 = (m-1)//25

for i in range(1,m+1):
    if pow(i,p1,m) == 1 or pow(i,p2,m) == 1 or pow(i,p3,m) == 1 or pow(i,p4,m) == 1:
        continue
    else:
        print(i)