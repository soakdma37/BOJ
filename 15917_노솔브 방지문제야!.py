import sys
input=sys.stdin.readline
l=[2**i for i in range(32)]
q=int(input())
for j in range(q):
    a=int(input())
    if a in l:print(1)
    else:print(0)