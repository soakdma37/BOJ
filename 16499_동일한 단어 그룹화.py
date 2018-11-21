a=int(input())
l=[]
testL=[]
for i in range(a):
    word=input()
    tmp=list(word)
    tmp.sort()
    if tmp not in testL:
        testL.append(tmp)
        l.append(word)
print(len(l))
