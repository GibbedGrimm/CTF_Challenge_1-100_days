from math import gcd

with open("cheese.txt") as f:
    ct = f.readline().strip()     # например DKLUUVY
    pt = f.readline().strip()     # например cheddar
    ctFlag = f.readline().strip() # например CYZRVTLGCYVBPKUE
ct = ct.lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"

charToIndex = {c: i for i, c in enumerate(alphabet)}

m = 26
x1,y1 = charToIndex[pt[0]],charToIndex[ct[0]]
x2,y2 = charToIndex[pt[1]],charToIndex[ct[1]]

#(y1-y2) = a * (x1-x2) mod 26
diffX = (x1-x2)%m
diffY = (y1-y2)%m

invDiffX = pow(diffX,-1,m)
a = (diffY*invDiffX)%m

b = (y1 -(x1*a))%m
print(a,b)
