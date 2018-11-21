from math import sqrt as s
a=(1+s(5))/2
b=(1-s(5))/2
n=int(input())
r=((a**n-b**n)//s(5))%1000000
print(int(r))