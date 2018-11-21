a=input()
n=0
for i in range(len(a)):
    try:
        int(a[i])
        n+=int(a[i])*(16**(len(a)-i-1))
    except:
        if a[i]=="A":n+=10*(16**(len(a)-i-1))
        elif a[i]=='B':n+=11*(16**(len(a)-i-1))
        elif a[i]=='C':n+=12*(16**(len(a)-i-1))
        elif a[i]=='D':n+=13*(16**(len(a)-i-1))
        elif a[i]=='E':n+=14*(16**(len(a)-i-1))
        elif a[i]=='F':n+=15*(16**(len(a)-i-1))
print(n)