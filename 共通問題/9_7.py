def count(num):
    x=int(input('整数を入力してください：',))
    if x in num:
        return print(x,'は配列に含まれています。')
    else:
        return print(x,'は配列に含まれていません。')

num=[4,10,59,679,1991,3994,6789,19324]
count(num)