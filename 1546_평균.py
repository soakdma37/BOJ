n=input()
scores=list(map(int,input().split()))
maxScore=max(scores)
newScores=[]
for i in scores:
    newScores.append(100*(i/maxScore))
newAvg=sum(newScores)/len(newScores)
print(newAvg)