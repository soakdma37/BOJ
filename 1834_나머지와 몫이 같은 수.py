a=int(input())
numList=[]
for i in range(1,a):
    numList.append(a*i+i)
ans=sum(numList)
print(ans)