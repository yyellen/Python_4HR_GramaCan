# 類別 class、物件 object
# 物件函式 在物件裡面宣告函式來做使用

class Phone:
    def __init__(self, os, number, is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof
    
    def is_iOS(self):
        if self.os == "iOS":
            return True
        else:
            return False
    
    def add(self, num1, num2):
        return num1 + num2

phone1 = Phone("iOS", 123, True)
print(phone1.is_iOS()) # True
print(phone1.add(5, 6)) # 11