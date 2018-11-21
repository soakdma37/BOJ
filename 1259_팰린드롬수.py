while 1:
    s=input()
    if s=='0':break
    else:
        if s==s[::-1]:print('yes')
        else:print('no')