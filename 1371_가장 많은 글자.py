D={}
for i in range(97,123):
    D[chr(i)]=0
while 1:
    try:
        a=input()
        for i in range(97,123):D[chr(i)]+=a.count(chr(i))
    except:break
maxvalue=max(D.values())
result=""
for i in D:
    if D[i]==maxvalue:
        result+=i
print(result)