# 類別 class、物件 object

class Phone:
    def __init__(self, os, number, is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof

phone1 = Phone("iOS", 123, True)

print(phone1.os)
print(phone1.number)
print(phone1.is_waterproof)

phone2 = Phone("Android", 456, False)

print(phone2.os)
print(phone2.number)
print(phone2.is_waterproof)