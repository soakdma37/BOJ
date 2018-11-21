d={}
n,m=map(int,input().split())
for i in range(n):
    d[input()]=1
l=[]
c=0
for i in range(m):
    a=input()
    try:
        if d[a]==1:
            l.append(a)
            c+=1
    except:
        pass
l.sort()
print(c)
for i in l:
    print(i)