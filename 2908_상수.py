a,b=input().split()
ra="".join(reversed(list(a)))
rb="".join(reversed(list(b)))
l=[int(ra),int(rb)]
print(max(l))