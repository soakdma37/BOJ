def checkPrime(n):
    if n==1:return False
    elif n==2:return True
    result=True
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            result=False
            break
    return result

m,n=map(int,input().split())
for i in range(m,n+1):
    if checkPrime(i):
        print(i)