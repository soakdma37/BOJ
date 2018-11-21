import sys
input=sys.stdin.readline
n,k=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
print(l[k-1])