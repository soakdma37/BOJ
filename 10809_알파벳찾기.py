w=input()
a=[]
for i in range(97,123):
        a.append(str(w.find(chr(i))))
print(" ".join(a))