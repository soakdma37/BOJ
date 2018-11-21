n=int(input())
s=list({input() for i in range(n)})
s.sort(key=lambda x:(len(x),x))
for i in s:
    print(i)