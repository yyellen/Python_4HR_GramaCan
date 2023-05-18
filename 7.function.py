# 函式 function: 函式的定義 函式的呼叫
def hello(name, age):
    print("hello" + name + "你今年" + age + "歲")

hello("小白", "27")
# 先定義一個函式 才能呼叫他


# ---------------------------------------------------------------------------- #
def add(num1, num2):
    # print(num1+num2)
    # return 10 # 10 return 會覆蓋add(5,8)
    return num1+num2

print(add(5,8)) # 13


# ---------------------------------------------------------------------------- #
# 預設會 return None
def add(num1, num2):
    print(num1+num2) # 13
    # return None # 預設會 return None

value = add(5,8)
print(value) # None


# ---------------------------------------------------------------------------- #
# 函式遇到 retuen 就會停止，不會繼續往下執行
def add(num1, num2):
    print(num1+num2) # 13
    return 10 # 10
    print("你好") # 不會執行

value = add(5,8)
print(value)
