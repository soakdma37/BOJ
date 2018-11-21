import math

def checkPrime(n):
    if n==1:return False
    elif n==2:return True
    result=True
    for i in range(2,math.ceil(math.sqrt(n))+1):
        if n%i==0:
            result=False
            break
    return result

while 1:
    tc=int(input())
    if tc==0:
        break
    else:
        l=[]
        for i in range(tc+1,2*tc+1):
            if checkPrime(i):l.append(i)
        print(len(l))


