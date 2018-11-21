a=input()
l=[]
for i in range(len(a)):l.append(a[i:])
l.sort()
for i in l:print(i)