import sys
input=sys.stdin.readline
r,c,q=map(int,input().split())
l=[]
for i in range(r):
    l.append(list(map(int,input().split()))) #각 행 저장
for i in l:
    for j in range(1,len(i)):
        i[j]+=i[j-1] #l 안의 리스트들의 원소를 부분합으로 만듬
for i in range(q):
    r1,c1,r2,c2=map(int,input().split()) #직사각형 꼭짓점 입력
    pixelSum=0 #주어진 픽셀들 밝기합
    pixelNum=(r2-r1+1)*(c2-c1+1)
    tmp1=l[r1-1:r2] #주어진 행만 잘라내기
    if c1==1:
        for z in tmp1:
            pixelSum+=z[c2-1]
    else:
        for z in tmp1:
            pixelSum+=(z[c2-1]-z[c1-2])
    print(pixelSum//pixelNum)