a=int(input())
l=[]
while a>0:
    l.append(str(a%9))
    a=a//9
l.reverse()
print("".join(l))