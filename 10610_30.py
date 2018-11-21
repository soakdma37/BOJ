n=list(map(int,list(input())))
if 0 in n and sum(n)%3==0:
    n.sort(reverse=True)
    n=list(map(str,n))
    n="".join(n)
    print(n)
else:print(-1)
