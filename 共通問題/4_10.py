print('0～100 までの得点（整数値）を入力してください')
n=int(input())
if n > 100 or n < 0:
    print('入力値が不正です')
else:
   print('正しい入力値です')