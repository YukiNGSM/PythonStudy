array=[]
sum=0
import random
for i in range(10):
    x=random.randint(0,99)
    array.append(x)
    sum+=x
    maxi=max(array)
print('合計値は',sum,'です。')
print('最大値は',maxi,'です。')
for j in range(10):
    print('配列[',j,']:',x,sep='')