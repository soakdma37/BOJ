D={1:9,2:17}
n=int(input())
for i in range(2,n+1):
    D[i]=2*D[i-1]-2
print(D[n]%1000000000)