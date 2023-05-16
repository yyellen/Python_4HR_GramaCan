# 如何使用數字
print(77)
print(-77.5)
print(8+5) # 13
print(8-5) # 3
print(8*5) # 40
print(2**5) # 32 次方
print(8/5) # 1.6
print(8//5) # 1 除法取整數
print(8%5) # 3 餘數
print(8+8*5) # 48 先乘除後加減
print((8+8)*5) # 80 括號內先運算

number = 8
print(number*5) # 40

# 函式 function
print("會印出數字" + str(number)) # 會印出數字8
print(8 + str(number)) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

number = -8
print(abs(number)) # 8 絕對值

print(pow(2, 5)) # 32 次方

print(max(2, 3, 88, 100, 33, 52, 11, 78, 111, -100)) # 111
print(min(2, 3, 88, 100, 33, 52, 11, 78, 111, -100)) # -100

print(round(4.4)) # 4 四捨五入
print(round(4.6)) # 5
print(round(-4.4)) # -4
print(round(-4.6)) # -5

from math import *
print(floor(4.6)) # 4 無條件捨去
print(round(5.1)) # 5

print(ceil(5.1)) # 6 無條件進位

print(sqrt(64)) # 8.0 開根號