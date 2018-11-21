def d(n): #self number 만들기
    s=str(n)
    result=n
    for i in range(len(s)):
        result+=int(s[i])
    return result

selfnumDic={}
for i in range(10000):
    selfnumDic[i]=d(i)
aL=list(range(1,10001))
for i in selfnumDic.values():
    if i in aL:aL.remove(i)
for i in aL:
    print(i)