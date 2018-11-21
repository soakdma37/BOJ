testNum=int(input())
for i in range(testNum):
    iterNum,word=input().split()
    iterNum=int(iterNum)
    newWordL=[]
    for singleChr in word:
        newWordL.append(singleChr*iterNum)
    newWord="".join(newWordL)
    print(newWord)