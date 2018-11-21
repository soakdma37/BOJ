memo = {0:0,1:1,2:1}
def s(n):
    if n in memo:return (memo[n]%1000000009)
    else:
        for i in range(3,n):
            memo[i]=memo[i-1]+memo[i-3]
        return ((memo[n-1]+memo[n-2]+memo[n-3])%1000000009)
print(s(int(input())))