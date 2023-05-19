# 猜數字遊戲

import random

secret_num = random.randint(1, 100)
guess = None
guess_count = 0
guess_limit = 3
out_of_limit = False

# print(secret_num)

while secret_num != guess and not(out_of_limit):
    guess_count += 1
    if guess_count <= guess_limit:
        guess = int(input("請輸入數字:"))
        if guess > secret_num:
            print("小一點")
        elif guess < secret_num:
            print("大一點")
    else:
        out_of_limit = True

if out_of_limit:
    print("挑戰失敗，正確答案是" + str(secret_num))
else:
    print("恭喜你挑戰成功!")