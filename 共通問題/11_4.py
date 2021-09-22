from os import sep
import random
sum=0

class coins_name:
    fhun=0
    hun=0
    ft=0
    ten=0
    five=0
    one=0

class Coin:
    def addCoins(self):
        play=int(input)
        for i in range(play):
            random.randint(0,5)
            if i==0:
                coins_name.fhun=coins_name.fhun+1
            elif i==1:
                coins_name.hun=coins_name.hun+1
            elif i==2:
                coins_name.ft=coins_name.ft+1
            elif i==3:
                coins_name.ten=coins_name.ten+1
            elif i==4:
                coins_name.five=coins_name.five+1
            elif i==5:
                coins_name.one=coins_name.one+1
    sum=(500*coins_name.fhun)+(100*coins_name.hun)+(50*coins_name.ft)+(10*coins_name.ten)+(5*coins_name.five)+(1*coins_name.one)
            

    def getCount(self):
        x=int(input("1~500円までの硬貨で知りたい硬貨の枚数"))
        if x==0:
            print('500円:',coins_name.fhun,'枚',sep='')
        elif x==1:
            print('100円:',coins_name.hun,'枚',sep='')
        elif x==2:
            print('50円:',coins_name.ft,'枚',sep='')
        elif x==3:
            print('10円:',coins_name.ten,'枚',sep='')
        elif x==4:
            print('5円:',coins_name.five,'枚',sep='')
        elif x==5:
            print('1円:',coins_name.one,'枚',sep='')

    def getAmount(self):

        calc=Coin()
        total=calc.addCoins(sum)
        print('総額:{}円'.format(total),)

main=Coin()
main.getAmount


