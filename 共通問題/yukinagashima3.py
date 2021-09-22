#3_1~6
print(12+34)
print(98-76)
print(23*45)
print(56//14)
print(66//9)
print(7%3)

#3_7~9
print(6*5//2,)
print((8+5)*6//2)
pi=3.14
print(pi*3**2)

#3_10
x='abc'
y='xyz'
print(x+y)

#省略
#3_19
print('BMI 値を求めます')
x=int(input('身長(cm):'))
y=int(input('体重(Kg)'))
print('BMI値 = ',65/((175/100)**2))

#3_20
x=450
y=200
z=100
sum=x+y+z
tax=int(sum*0.1)
chip=int(sum*0.16)
allsum=int(sum+chip+tax)
print('ハンバーガー  ：',x)
print('シェイク　　  ：',y)
print('コーラ 　　　 ：',z)
print('合計額（税抜）：',sum)
print('消費税 　　　 ：',tax)
print('チップ       ：',chip)
print('合計額（税込）：',allsum)

#3_21
import random
num1=random.randint(0,9)
num2=random.randint(0,9)
num3=random.randint(0,9)
num4=random.randint(0,9)
all=num1+num2*num3-num4
print(num1,'+',num2,'×',num3,'-',num4,'=')
x=print(input('計算結果は？:'))
if x==all:
    print('正解です！')
else:
    print('不正解です。正解は',all,'です。',sep='')
