D={1:1,2:1,3:1}
def f(n):
    if n in D:return D[n]
    else:
        for i in range(4,n+1):
            D[i]=D[i-1]+D[i-3]
        return D[n]
a=int(input())
print(f(a))