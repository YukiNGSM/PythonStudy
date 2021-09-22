#14_1
x=str(input('文字列を入力：'))
print(x)

#14_4
print('文字列を２つ入力してください。')
x=str(input('１つ目文字列を入力：'))
y=str(input('２つ目文字列を入力：'))
if x==y:
    print('同じ文字列です。')

#14_12
address = input("住所を入力してください：")
index = 0
if address.find("東京都") != -1:
    index = address.find("都")
elif address.find("北海道") != -1:
    index = address.find("道")
elif address.find("大阪府") != -1 or address.find("京都府") != -1:
    index = address.find("府")
elif address.find("県") != -1:
    index = address.find("県")
print(address[index+1:])
