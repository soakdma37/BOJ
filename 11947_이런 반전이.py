def f(n): #반전수 구하기
    return(int('9'*len(str(n)))-n)
t=int(input())
for i in range(t):
    a=int(input())
    l=len(str(a)) #input자릿수
    c=5*pow(10,l-1) #반전수와의 곱은 그 자릿수의 중간값(5,50,500...)에서 가장 크다
    if a>c:
        m=c*f(c)
    else:
        m=a*f(a)
    print(m)