caseNum=int(input())
for i in range(caseNum):
    studentScores=list(map(int,input().split()))
    studentNum=studentScores.pop(0)
    avg=sum(studentScores)/studentNum

    overStudent=[]
    for score in studentScores:
        if score>avg:
            overStudent.append(score)
    overPercent=len(overStudent)/studentNum
    print("%.3f%%"%(overPercent*100))