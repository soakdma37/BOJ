import sys
input=sys.stdin.readline
f={0:1,1:1,2:2,3:6,4:24,5:120,6:720,7:5040,8:40320,9:362880}
while 1:
    a=input().replace("\n","")
    l=len(a)
    if a=='0':break
    else:
        c=0
        for i in range(l):
            c+=(int(a[i])*f[l-i])
        print(c)
