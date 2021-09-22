num = int(input("数値入力："))
is_prime = True

for i in range(2, num):
    if num % i == 0:
        print(str(num), "は素数ではありません。", )
        is_prime = False
        break

if is_prime:
    print(str(num), "は素数です。")