import math

class Circle:
    PI=3.1415

    def calc_enshu(self,r):
        res=2*Circle.PI*r
        return math.floor(res*10**3)/(10**3) #少数第3位の表示

    def calc_menseki(self,r):
        res=Circle.PI*r**2
        return math.floor(res*10**3)/(10**3)

class Main:

    def execute(self):
        circle=Circle()
        r=int(input('半径を整数値で入力：'))
        enshu=circle.calc_enshu(r)
        menseki=circle.calc_menseki(r)

        print("円周の長さは{}です。".format(enshu))
        print("円の面積は{}です。".format(menseki))

main=Main()
main.execute()
