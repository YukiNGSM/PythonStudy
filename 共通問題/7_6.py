sum=0
ave=0
co=0
while True:
    n=int(input('整数を入力:'))
    co+=1
    sum+=n
    if n==0:
        break
ave=round(sum/co)
print('合計値:',sum)
print('平均値:',ave)