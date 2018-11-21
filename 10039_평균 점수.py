scoreList=[]
for i in range(5):
    a=int(input())
    if a<40:
        a=40
    scoreList.append(a)
avg=sum(scoreList)/5
print(int(avg))