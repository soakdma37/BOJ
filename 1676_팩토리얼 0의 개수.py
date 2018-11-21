import math
n=str(math.factorial(int(input())))
count=0
for i in range(len(n)-1,0,-1):
    if n[i]=='0':
        count+=1
    else:break
print(count)