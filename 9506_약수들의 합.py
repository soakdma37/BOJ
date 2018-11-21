def f(n):
    l=[]
    for i in range(1,int(n**.5)+1):
        if n%i==0:
            l+=[i,n//i]
    l.remove(n)
    return sorted(l) #약수들이 정수형태로 정렬되어 들어 있는 리스트
while 1:
    a=int(input())
    if a==-1:break
    elif a==sum(f(a)):
        print("%d = %s"%(a," + ".join(map(str,f(a)))))
    else:
        print("%d is NOT perfect."%a)
