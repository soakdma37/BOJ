a,b,c=map(int,input().split())
if c==1:
    a=a^b
elif c%2==0:
    for i in range(c//2):a=(a^b)^b
else:
    for i in range(c//2):a=(a^b)^b
    a=a^b

print(a)