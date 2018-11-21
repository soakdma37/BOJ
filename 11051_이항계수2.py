from math import factorial
n,k=map(int,input().split())
r=factorial(n)//(factorial(k)*factorial(n-k))
print(int(r)%10007)