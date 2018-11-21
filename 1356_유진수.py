a=input()
r="NO"
for i in range(len(a)):
    c1,c2=1,1
    for z in a[:i]:
        c1*=int(z)
    for x in a[i:]:
        c2*=int(x)
    if c1==c2 and a!='1':r="YES"
print(r)