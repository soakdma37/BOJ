month,day=map(int,input().split())
weekdayDic={0:"MON",1:"TUE",2:"WED",3:"THU",4:"FRI",5:"SAT",6:"SUN"}
monthNumDic={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
overDay=0
if month>1:
    for i in range(1,month):
        overDay+=monthNumDic[i]
overDay+=(day-1)
result=weekdayDic[overDay%7]
print(result)


