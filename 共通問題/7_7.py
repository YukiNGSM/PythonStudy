sum=0
co=0
while True:
    n=int(input('整数を入力:'))
    if n<0:
        continue
    elif n==0:
        break
    co+=1
    sum+=n
print('合計値:',sum)
print('平均値:',sum/co)