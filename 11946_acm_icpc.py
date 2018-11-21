TimeD={} #걸린시간저장
SolvedD={} #푼문제리스트저장
TeamWrongD={} #팀별로 그 문제 틀린 횟수 저장
n,m,q=map(int,input().split()) #팀갯수 n팀, 문제수 m문제, 채점로그 q개
for i in range(1,n+1):
    TimeD[str(i)]=0 #모든 팀의 총시간, 푼문제 0, 문제별 틀린횟수 0으로 초기값을 설정
    SolvedD[str(i)]=[]
    TeamWrongD[str(i)]={}
for i in range(1,m+1):
    for j in TeamWrongD:
        TeamWrongD[j][str(i)]=0 #각 팀의 모든 문제 틀린 횟수를 0으로 초기화
    #TeamWrongD[팀번호]={문제번호:그팀이 틀린횟수}
for i in range(q): #q개 채점
    TimeSpent,TeamNum,ProbNum,Result=input().split() #입력은 모두 문자열 type로 저장
    if ProbNum not in SolvedD[TeamNum] and Result!='AC':
        #지금까지 그문제 못풀었고 AC가 아니면 소비시간 ++. 그문제 틀린횟수 ++
        TeamWrongD[TeamNum][ProbNum]+=1
    if ProbNum not in SolvedD[TeamNum] and Result=='AC':
        #지금까지 그문제 못풀었고 AC면 소비시간 ++,푼문제리스트에 추가
        TimeD[TeamNum]+=(int(TimeSpent)+20*TeamWrongD[TeamNum][ProbNum])
        SolvedD[TeamNum].append(ProbNum)
TeamInfoL=[]
for i in range(1,n+1): # [팀번호,푼문제수,걸린시간]
    TeamInfoL.append([i,len(SolvedD[str(i)]),TimeD[str(i)]])
TeamInfoL.sort(key=lambda x:((-1)*x[1],x[2],x[0]))
#푼문제 수 내림차순-> 총 시간 오름차순 -> 팀번호 오름차순 정렬
for info in TeamInfoL:
    print(" ".join(str(z) for z in info))


