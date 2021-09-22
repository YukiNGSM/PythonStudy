
print('合計点と平均点を求めます。')
math=int(input('学生の人数:'))
sum=0
y=0
len=0
for i in range(math):
    y+=1
    print(y,'番目の点数:',end='')
    point=int(input())
    sum+=point
    len+=1
print('合計は',sum,'点です。',sep='')
print('平均は',sum/len,'点です。',sep='')