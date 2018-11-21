def people(k,n): #k층 n호의 사람수 구하기
    D={}
    D[0]=[i for i in range(1,n+1)] #0층의 i호엔 i명의 사람이 산다(그러나 인덱스는 0부터..)
    r=0 #k층 n호의 사람수
    for z in range(1,k+1): #k층까지 루프
        D[z]=[sum(D[z-1][:x]) for x in range(1,n+1)] #z층의 n호까지의 사람수
    return D[k][n-1]

q=int(input())
for i in range(q):
    n=int(input())
    k=int(input())
    print(people(n,k))