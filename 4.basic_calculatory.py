# 建立一個基本計算機
# name = input("請輸入你的名字:")
# age = input("請輸入你的年紀:")
# print("哈囉" + name + " 你今年" + age + "歲")

number1 = input("請輸入第一個數字: ") # 8
number2 = input("請輸入第一個數字: ") # 5.5
# print(number1 + number2) # "85.5" input預設為字串
# print(int(number1) + int(number2)) # ValueError: invalid literal for int() with base 10: '5.5' int是轉換成整數
print(float(number1) + float(number2)) # 13.5
