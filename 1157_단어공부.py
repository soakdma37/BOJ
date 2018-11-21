AlphaList=[chr(i) for i in range(97,123)]
word=input()
maxused='a'
for i in AlphaList:
    if word.count(i)+word.count(i.upper())>word.count(maxused)+word.count(maxused.upper()):
        maxused=i
#이때 maxused는 가장 많이 사용된 알파벳
AlphaList.remove(maxused)
usedNumList=[]
for i in AlphaList:
    usedNumList.append(word.count(i)+word.count(i.upper()))
if word.count(maxused)+word.count(maxused.upper()) in usedNumList:
    print("?")
else:print(maxused.upper())


