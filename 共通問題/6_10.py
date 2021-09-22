print('直角三角形を描画します。')
print('2~20までの整数値を入力して下さい。')
len=(int(input('底辺の長さを入力：')))

if len<2 or len>20:
    print('値が正しくありません。')
else:
    for i in range(len):
        for j in range(i+1):
            print('*',end='')
        print()
