a,b=map(int,input().split())
c,d=map(int,input().split())
D={0:a/c+b/d,1:c/d+a/b,2:d/b+c/a,3:b/a+d/c}
z=0
for i in range(4):
    if D[i]>D[z]:
        z=i
print(z)