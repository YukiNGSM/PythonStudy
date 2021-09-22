import random
num1=random.randint(1,9)
num2=random.randint(1,9)
num3=random.randint(1,9)
num4=random.randint(1,9)
print(num1,'+',num2,'×',num3,'-',num4,'=')
ans=str(num1+num2*num3-num4)

n=int(input('計算結果は？'))
if n!=ans:
    print('正解です！')
else:
    print('不正解です。正解は',ans,'です。')