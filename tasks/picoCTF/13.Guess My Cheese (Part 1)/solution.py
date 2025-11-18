
ct = "KPMLLIZ"
ctf = "ILMTWABONT"
#RAGDYQFPQFYAZFNDUEAZIFH
pt = 'CHEDDAR'
ptf = ''
alphabet = 'abcdefghijklmnopqrstuvwxyz'.upper()
indexed = {c:i for i,c in enumerate(alphabet)}
x1,y1 = indexed[pt[0]],indexed[ct[0]]
x2,y2 = indexed[pt[1]],indexed[ct[1]]
diffx = (x1-x2)%26
diffy = (y1-y2)%26
invdiffx = pow(diffx,-1,26)
a = (invdiffx*diffy)%26
b = (y1-x1*a) %26
inva = pow(a,-1,26)
for i in range(len(ct)):

    x = indexed[pt[i]]
    y = (x*a+b)%26
    if ct[i] != alphabet[y]:
        print('Ошибка',ct[i],alphabet[y],x,y,a,b)
        break
else:
    for i in range(len(ctf)):
        y = indexed[ctf[i]]
        x = (((y-b)%26)*inva)%26

        ptf+=alphabet[x]
print(ptf)
