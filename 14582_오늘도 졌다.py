a=list(map(int,input().split()))
b=list(map(int,input().split()))
r="No"
for i in range(10):
    if sum(a[:(i+1)])>sum(b[:i]):
        r="Yes"
        break
print(r)