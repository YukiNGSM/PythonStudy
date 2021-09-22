# hensu1をhensu2という名前で受け取って1プラスする
def kansu(hensu2):
    hensu2 += 1

# hensu1に100を入れて関数kansuにhensu1を渡す
hensu1 = 100
kansu(hensu1)

# hensu1の値を画面に出す。
print(hensu1)

# hensu1=100,
# hensu2=100+1,
# hensu1=100
del kansu

def kansu(hensu2):
    hensu2[0] += 1

hensu1 = [100]
kansu(hensu1)

print(hensu1[0])

del kansu

""""""
def kansu(hensu2):
    hensu2 += 1

hensu1 = [100]
kansu(hensu1[0])

print(hensu1[0])
