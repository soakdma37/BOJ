def f(n):
    l=[]
    for i in range(1,int(n**.5)+1):
        if n%i==0:
            if i!=n//i:
                l+=[i,n//i]
            else:
                l+=[i]
    l.remove(n)
    return sorted(l) #진약수들이 정수형태로 정렬되어 들어 있는 리스트

T=int(input())
L=list(map(int,input().split()))
for i in L:
    s=sum(f(i))
    if i==s:print("Perfect")
    elif i>s:print("Deficient")
    elif i<s:print("Abundant")