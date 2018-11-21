D={'black':0,'brown':1,'red':2,'orange':3,'yellow':4,'green':5,
    'blue':6,'violet':7,'grey':8,'white':9}
a1=input()
a2=input()
a3=input()
r=(D[a1]*10+D[a2])*(10**D[a3])
print(r)