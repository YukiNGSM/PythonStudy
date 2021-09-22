class SumCal:

    def __init__(self,x,y):
        self.x=x
        self.y=y

    def exe(self):
        sum=0
        
        for num in range(self.x,self.y+1):
            sum+=num
        return sum

class Main:

    def exePrint(self):
        calc=SumCal(100,200)
        total=calc.exe()
        print("{}から{}までの合計値は{}です。".format(calc.x,calc.y,total))
    
main=Main()
main.exePrint()