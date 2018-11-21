opcodeDic={'ADD':'00000','ADDC':'00001','SUB':'00010','SUBC':'00011',
           'MOV':'00100','MOVC':'00101','AND':'00110','ANDC':'00111',
           'OR':'01000','ORC':'01001','NOT':'01010','MULT':'01100',
           'MULTC':'01101','LSFTL':'01110','LSFTLC':'01111','LSFTR':'10000',
           'LSFTRC':'10001','ASFTR':'10010','ASFTRC':'10011',
           'RL':'10100','RLC':'10101','RR':'10110','RRC':'10111'}
binDic={'0':'000','1':'001','2':'010','3':'011','4':'100','5':'101',
        '6':'110','7':'111','8':'1000','9':'1001','10':'1010','11':'1011',
        '12':'1100','13':'1101','14':'1110','15':'1111'}

def trans(s): #문자열을 받는다.
    result=""
    s=s.split() #[opcode,rD,rA,rB] 인 리스트
    result+=(opcodeDic[s[0]]+'0') #opcode 처리
    result+=(binDic[s[1]]+binDic[s[2]]) #rD,rA 처리
    if s[0][-1]=='C': #C 가 주어지는 경우 opcode의 끝이 C임
        a=binDic[s[3]]
        if len(a)==3:
            a='0'+a
        result+=a
    else: #rB 가 주어지는 경우
        result+=(binDic[s[3]]+'0')
    return result


n=int(input())
for i in range(n):
    print(trans(input()))