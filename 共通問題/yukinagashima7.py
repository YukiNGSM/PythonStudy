#7_1
x=0
sum=0
while x<100:
    x+=1
    sum+=x
print('合計：',sum,sep='')

#7_7
sum=0
ave=0
while True:
    x=int(input('整数を入力：'))
    if x>1:
        sum+=x
    elif x==0:
        break
ave=sum//x
print('合計値：',sum)
print('平均値：',ave)
