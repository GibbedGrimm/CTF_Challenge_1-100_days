from sympy import *
m = 28151
f = []
numToCheck = []
for i in range(m):
    f.append(i)
    numToCheck.append(i)

for i in numToCheck:
    check = f.copy()
    print("Проверенно",i)
    for j in range(m):
        num = pow(i,j,m)
        if num not in check:

            break
        check.remove(num)
    else:
        print(i)
        break
