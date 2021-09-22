def plus(x,y):
    return x+y
def minus(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    if y==0:
        return print('無効')
    else:
        return x//y
def remainder(x,y):
    if y==0:
        return print('無効')
    else:
        return x%y
    
x=int(input('整数を入力してください：'))
y=int(input('整数を入力してください：'))

print(x,'+',y,'=',plus(x,y),sep='')
print(x,'-',y,'=',minus(x,y),sep='')
print(x,'*',y,'=',multiplication(x,y),sep='')
print(x,'/',y,'=',division(x,y),sep='')
print(x,'%',y,'=',remainder(x,y),sep='')