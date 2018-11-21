t=int(input())
a=0;b=0;c=0
if (t%10)!=0:print(-1)
else:
    while t>=300:
        t-=300
        a+=1
    while t>=60:
        t-=60
        b+=1
    c=(t//10)
    print("%d %d %d"%(a,b,c))
