a=int(input())
b=a
count=0
while 1:
    a=((a//10)+(a%10))%10+((a%10)*10)
    count+=1
    if a==b:
        break
print(count)