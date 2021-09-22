print('0～100 までの得点（整数値）を入力してください')
n=int(input('整数'))
if n == 100:
    print('満点合格です')
elif n < 100 and n > 60:
    print('合格です')
else: print('不合格です')