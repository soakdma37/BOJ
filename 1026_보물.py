n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
a.reverse()
b.sort()
r=0
for i in range(n):
    r+=a[i]*b[i]
print(r)