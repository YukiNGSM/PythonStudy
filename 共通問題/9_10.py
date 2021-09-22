def BMI(cmeter,gram):
    BMI = gram / ((cmeter / 100) ** 2)
    return BMI

def Normal(cmeter):
    normal = ((cmeter / 100) ** 2) * 22
    return normal

cmeter = float(input('身長(cm)を入力してください：'))
gram = float(input('体重(㎏)を入力してください：'))

BMI = BMI(cmeter,gram)
print('BMI 値は',"{:.2f}".format(BMI),'です',sep='')
Normal = Normal(cmeter)
print('適正体重は',"{:.2f}".format(Normal),'kgです',sep='')