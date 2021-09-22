#6_1
for i in range(10):
    print('for 文のプログラムです。')

#6_6
x=int(input('開始数：'))
y=int(input('終了数：'))
sum=0
for i in range(x,y+1):
    sum+=i
print('合計:',sum)

#6_9
for i in reversed(range(1,10,2)):
    print(i,'の段',sep='')
    for j in range(1,10):
        print(i,'×',j,'=',i*j)

#6_12 時間がかかるため省略
#for i in range(10):
#    print('*')
#    for j in range()