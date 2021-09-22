f=open('16_4write.txt','w')

while True:
    moji=str(input('入力：'))
    if moji=='end':
        break
    print(moji)

print('書き込み終了')
