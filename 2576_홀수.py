l=[]
for i in range(7):
    a=int(input())
    if a%2==1:
        l.append(a)
if l:
    print(sum(l))
    print(min(l))
else:print(-1)
