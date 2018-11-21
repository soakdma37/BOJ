D={1:1,2:1,3:1,4:2,5:2}
def P(n):
    if n in D:
        return D[n]
    else:
        for i in range(6,n+1):
            D[i]=D[i-1]+D[i-5]
        return D[n]
t=int(input())
for i in range(t):
    n=int(input())
    print(P(n))
