def check(num): #숫자 입력받자
    if "666" in str(num):
        return True
    else:
        return False

a=int(input())
resultList=[]
result=666
while len(resultList)<a:
    if check(result):
        resultList.append(result)
    result+=1
print(resultList[-1])