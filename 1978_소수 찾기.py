import math
def checkPrime(n):
    if n==2:return True
    elif n==1:return False
    result=True
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if n%i==0:
            result=False
            break
    return result

n=int(input())
li=list(map(int,input().split()))
count=0
for j in li:
    if checkPrime(j):
        count+=1
print(count)