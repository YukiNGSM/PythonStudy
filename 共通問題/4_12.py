n=int(input('西暦4桁'))
if n % 4==0 or not n % 100==0 and n % 400==0: print('閏年です')
else: print('平年です') 