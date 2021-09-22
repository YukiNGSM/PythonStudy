print('長方形を描画します。')
print('2~20までの整数値を入力してください。')

side=int(input('行数の入力：'))
if side<2 or side>20:
    print('値が正しくありません。')
else:
    main=int(input('列数の入力：'))
    if main<2 or main>20:
        print('値が正しくありません。')
    else:
        for i in range(1,side+1):
            for j in range(main):
                print('*',end='')
            print()