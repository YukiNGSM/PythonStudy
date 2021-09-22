n=int(input('整数値:'))
if n>0: 
    if n % 2 ==0:
        print('その値は正の偶数です')
    else:
        print('その値は正の奇数です')
elif n==0:
    print('その値は0です')
else:
    print('その値は正ではありません')
print('プログラムを終了します')