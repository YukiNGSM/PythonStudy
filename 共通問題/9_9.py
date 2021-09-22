def cal():
    pi=3.14159
    pir=(r+r)*pi
    pir2=pi*r**2
    print('半径',r,'の円の円周は',round(pir,2))
    print('半径',r,'の円の面積は',round(pir2,2))

r=float(input('半径を入力してください：'))
cal()
