memoDic={0:0,1:1}
def fib(n):
    if n in memoDic:
        return memoDic[n]
    else:
        memoDic[n]=fib(n-1)+fib(n-2)
        return memoDic[n]

n=int(input())
print(fib(n))