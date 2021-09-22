print('0～100 までの得点（整数値）を２つ入力してください')
n=int(input('１つ目の得点：'))
m=int(input('２つ目の得点：'))
if m >=70 and n >= 70:
    print('合格')
else:
    print('不合格')