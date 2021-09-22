
def sum(num):
    sum=0
    for i in range(8):
        sum+=num[i]
    return sum

num=[4,10,59,679,1991,3994,6789,19324]
print('合計値 = ',sum(num))