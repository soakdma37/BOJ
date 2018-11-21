a=int(input())
l=[]
for i in range(a):
    l.append(int(input()))
l=set(l)
l=list(l)
l.sort()
for i in range(len(l)):
    print(l[i])
