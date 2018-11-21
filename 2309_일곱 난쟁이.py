l=[]
for i in range(9):
    l.append(int(input()))
s=sum(l)

for i in range(9):
    for j in range(i+1,9):
        if s-l[i]-l[j]==100:
            fake=[l[i],l[j]]
            break
l.remove(fake[0])
l.remove(fake[1])

l.sort()
for i in range(7):
    print(l[i])