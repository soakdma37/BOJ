word=input()
answer=0
caList=["c=","c-","dz=","d-","lj","nj","s=","z="]
for i in caList:
    answer+=word.count(i)
    word=word.replace(i,"!")
word=word.replace("!","")
answer+=len(word)
print(answer)