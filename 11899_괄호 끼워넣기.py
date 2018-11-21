a=input()
while '()' in a:
    a=a.replace("()","")
print(len(a))