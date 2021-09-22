from array import array


print('整数値を 3 つ入力してください。')
array=[]
for i in range(3):
    x=print(input(' 1つ目の整数値：'))
    array.append(x)
    minm=min(array)
    maxi=max(array)
print('最大値：',maxi)
print('最小値：',minm)
