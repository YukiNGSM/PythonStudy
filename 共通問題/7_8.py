num1=0
num2=0
loop=1
disp=''

while True:
    if loop==1:
        disp+=str(num1)
    elif loop==2:
        disp+=str(',')
        disp+=str(num2)
    else:
        num1,num2=num2,num1+num2
        if num2>1000:
            break

        disp+=str(',')
        disp+=str(num2)
        
    loop+=1

print(disp)
