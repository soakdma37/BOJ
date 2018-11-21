import sys
D={}
n=int(sys.stdin.readline())
for i in range(n):
    a=int(sys.stdin.readline())
    if a in D:D[a]+=1
    else:D[a]=1
for i in sorted(D.keys()):
    for j in range(D[i]):
        print(i)