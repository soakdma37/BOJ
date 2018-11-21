memo0={0:1,1:0}
memo1={0:0,1:1}
def count(n):
    if n in memo0 and n in memo1:
        return (memo0[n],memo1[n])
    else:
        for i in range(2,n+1):
            memo0[i] = memo0[i - 1] + memo0[i - 2]
            memo1[i] = memo1[i - 1] + memo1[i - 2]
        return (memo0[n],memo1[n])

a=int(input())
for i in range(a):
    tmp=int(input())
    print("%d %d"%(count(tmp)[0],count(tmp)[1]))