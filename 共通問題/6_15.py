sum=0
a=0
for i in range(10):
    print(i+1,'回目の入力：',end='')
    a=int(input())
    sum+=a
print('合計：',sum)