from array import array
from random import randint


sum=0
ave=0
array=[]
for i in range(5):
    x=int(input('整数:'))
    array.append(x)
    sum+=x
ave=sum/5
print('【実行結果】配列が',array,'の場合')
print('合計値は',sum,'です。')
print('平均値は',ave,'です。')