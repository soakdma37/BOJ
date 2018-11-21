l=[]
n=int(input())
t=0
tmpL=[] #지금까지 깨진 화분들에 쓰인 숫자 리스트
for i in range(n):
    l.append(input().split()) #화분들 입력받음
while t<len(l):
    tmpL=[]
    tmpL+=l[t]
    for l1 in l[t+1:]:
        for i in tmpL:
            if i in l1:
                tmpL+=l1
                l.remove(l1)
    t+=1
print(t)