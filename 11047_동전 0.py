n,k=map(int,input().split())
c=0
l=[int(input()) for i in range(n)]
for j in range(len(l)-1,-1,-1):
    c+=k//l[j]
    k%=l[j]
print(c)