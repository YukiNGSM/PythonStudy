#list
array=[10, -10, 40, -15, 90, 15, -80]
rearray=sorted(array,reverse=True)
print('ソート前：',sorted(array))
print('ソート後：',rearray)
del array,rearray

#tuple
array=10, -10, 40, -15, 90, 15, -80
rearray=sorted(array,reverse=True)
print('ソート前：',sorted(array))
print('ソート後：',rearray)