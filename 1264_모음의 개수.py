while 1:
    s=input()
    c=0
    if s=='#':break
    else:
        for i in 'aeiouAEIOU':
            c+=s.count(i)
        print(c)