def make1(n): #n을 1로 만드는 횟수 리턴
    D={1:0}
    for i in range(2,n+1):
        D[i]=D[i-1]+1
        if i%2==0:D[i]=min(D[i-1]+1,D[i//2]+1)
        if i%3==0:D[i]=min(D[i-1]+1,D[i//3]+1)
    return D[n]
print(make1(int(input())))