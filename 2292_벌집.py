n=int(input())
count=0
if n==1:count=1
elif n==2:count=2
else:
    for i in range(2,n):
        if 3*(i**2)-9*i+8<=n<3*(i**2)-3*i+2:
            count=i
            break

print(count)