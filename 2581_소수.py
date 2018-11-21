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

m=int(input())
n=int(input())
primeL=[]
answerList=[]
count=0
for i in range(10000):
    if checkPrime(i):
        primeL.append(i)

for i in range(m,n+1):
    if i in primeL:
        answerList.append(i)

if len(answerList)==0:print(-1)
else:
    print(sum(answerList))
    print(min(answerList))