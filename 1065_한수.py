def checkHan(num):
    strNum=str(num)
    if len(strNum)==1 or len(strNum)==2:
        return True
    else:
        result=True
        for i in range(len(strNum)):
            if int(strNum[i])-int(strNum[i-1])==int(strNum[i-1])-int(strNum[i-2]):
                result=True
            else:
                result=False
                break
        return result

a=int(input())
count=0
for i in range(1,a+1):
    if checkHan(i):
        count+=1
print(count)
