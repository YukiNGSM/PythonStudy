#文字列の連結
import abc


moji='_' * 10
print(moji)

#例
x='abc'
y='def'
haihun='_' * 10
print(x,y,haihun,sep='')
del moji

#インデックス pythonは添字0から
moji='abcdef'
print(moji[0])
print(len(moji))
for i in range(len(moji)):
    print(moji[i])
del moji

#文字列をスライス式で取り出す
s='abcdef'
print(s[1:5]) #左がはじまり,右が終わり
print(s[0:3:2]) #添字0～3までを2文字おきで取得
#その他のスライス式
#s[:]全部取り出す
#s[:n]先頭からn個取り出す
#s[i:]iから末尾まで取り出す
#s[-n]末尾からn個取り出す
#s[::k]k-1個取り出す
#s[::-1]全て逆に取り出す
del s

#文字列がその文字に含まれているか調べる
s='abcdef'
if 'bc' in s:
    print('変数sに含まれています')
del s

#enumerate関数での文字列走査
s='abcdef'
for i,ch in enumerate(s):
    print(i,ch)
del s

#ある文字列が出現するインデックス番号を調べる
s='abcdef'
print(s.index('cd'))
#その他
#1 .count(文字列)   変数内から文字列の出現数をカウント
#2 .replece(文字列、返還後の文字列)    文字列を変換
#3 .find(文字列)    文字列検索
#4 .rfind(文字列)   逆から文字列検索
#5 .strip(文字)     文字削除

print('こんに{}ちは'.format(s))
del s

a=10
b=20
print('こんに{1}ちは'.format(a,b))
print('こんに{ka}ちは'.format(ka=a))
#そのほか
#1 {:<10} 10桁として扱い、左揃えに指定
#2 {:>10} 10桁として扱い、右揃えに指定
#3 {:^10} 10桁として扱い、中央揃えに指定
#4 {:*10} 10桁として扱い、
#5 {:=10} 10桁として扱い、
#1 {:3d} 10進数を3桁分の幅を使って出力する指定
#2 {:3s} 文字列を3桁分の幅を使って出力する指定
#3 {;,} 3桁区切りのカンマ,付きに指定