#4_1
print('0～100 までの得点（整数値）を入力してください')
x=int(input())
if x>=80:
    print('合格です。')

#4_6
print('整数値を入力してください')
x=int(input())
if x%2==0:
    print('偶数です')
else:
    print('奇数です')

#4_12
x=int(input('西暦の入力'))
if x%400==0:
    print('閏年です')
    if x%10==0:
        print('平年です')
        if x%4==0:
            print('閏年です')
        else:
            print('平年です')