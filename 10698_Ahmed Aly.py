n=int(input())
for i in range(n):
    e=input()
    e=e.replace(" ","")
    eL=e.split("=")
    if eval(eL[0])==int(eL[1]):
        print("Case %d: YES"%(i+1))
    else:
        print("Case %d: NO"%(i+1))