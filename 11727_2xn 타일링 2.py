D={0:1,1:1}
n=int(input())
for i in range(2,n+1):
    D[i]=D[i-1]+2*D[i-2]
print(D[n]%10007)