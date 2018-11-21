import math

a=int(input())
for i in range(math.ceil(math.sqrt(a))):
    if (i**2)+i+1==a:
        r=i
        break
print(r)