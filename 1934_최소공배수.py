a=int(input())
for i in range(a):
    z,x=map(int,input().split())
    if z>x:
        z,x=x,z
    for j in range(1,z+1):
        if (x*j)%z==0:
            result=x*j
            break
    print(result)