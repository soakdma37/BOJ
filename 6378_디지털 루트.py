def droot(n): #문자열 타입을 입력받는 함수
    while len(n)>1:
        count=0
        for i in range(len(n)):
            count+=int(n[i])
        n=str(count)
    return n

while 1:
    a=input()
    if a=='0':break
    else:print(droot(a))