D={1:1,2:2,3:4}
for i in range(4,11):
    D[i]=D[i-1]+D[i-2]+D[i-3]
t=int(input())
for i in range(t):
    print(D[int(input())])