print('合計点と平均点を求めます。')
sum=0
y=0
len=0
while True:
    y+=1
    print(y,'番目の点数:',end='')
    point=input()
    if point.isnumeric():
        sum+=int(point)
        len+=1
    elif point=='End':
        break
print('合計は',sum,'点です。',sep='')
print('平均は',sum/len,'点です。',sep='')