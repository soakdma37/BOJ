a=input()
aL=a.split() #[k1,o1,k2,o2,k3]
aL=[w.replace("/","//") for w in aL]

r1=eval(aL[0]+aL[1]+aL[2]) #1번째 연산 계산 결과들
r2=eval(aL[2]+aL[3]+aL[4])

if r1<0 and aL[3]=="//": #피연산자 중 하나가 음수
    re1=(-1)*eval(str((-1)*r1)+aL[3]+aL[4])
else:
    re1=eval(str(r1)+aL[3]+aL[4])

if r2<0 and aL[1]=="//": #피연산자 중 하나가 음수
    re2=(-1)*eval(aL[0]+aL[1]+str((-1)*r2))
else:
    re2=eval(aL[0]+aL[1]+str(r2))

reL=[int(re1),int(re2)]
reL.sort()
for i in reL:
    print(i)

