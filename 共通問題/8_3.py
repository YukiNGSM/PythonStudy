even=[]
odd=[]
for i in range(10):
    num=int(input(str(i+1)+'件目：整数を入力　＝　'))
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print('偶数値配列 = ',even,)
print('奇数値配列 = ',odd,)
    