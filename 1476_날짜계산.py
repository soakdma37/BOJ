e,s,k=map(int,input().split())
y=1
if e == 15: e = 0
if s == 28: s = 0
if k == 19: k = 0
while 1:
    if y%15==e and y%28==s and y%19==k:
        break
    y+=1
print(y)