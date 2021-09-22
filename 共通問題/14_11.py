x=(input('住所を入力してください：'))
if '市' in x:
    print('市')
elif '郡' in x:
    print('郡')
else:
    print('東京 23 区')