n=int(input())
l=[input().split() for i in range(n)]
l.sort(key=lambda x:(int(x[0]),int(x[1])))
for l1 in l:
    print(" ".join(l1))