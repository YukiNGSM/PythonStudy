f=open('16_2.txt',encoding="utf-8_sig")

while True:
    line=f.readline()
    if not line:
        break
    print(line,end='')

f.close()