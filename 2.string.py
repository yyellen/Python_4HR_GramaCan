# 如何使用字串
print("Hello Mr.White")
print("Hello \nMr.White") # \n換行
print("Hello\" Mr.White") # Hello" Mr.White
print("Hello " + "Mr.White")

word = "Hello "
print(word + "Mr.White")

# 函式 function
phrase = "Hello Mr.White"
print(phrase.lower()) # hello mr.white
print(phrase.upper()) # HELLO MR.WHITE
print(phrase.isupper()) # False 判斷是不是全部都是大寫
print(phrase.islower()) # False 判斷是不是全部都是小寫
print(phrase.lower().islower()) # True
print(phrase[1]) # e
print(phrase[0]) # H
print(phrase.index("H")) # 0
print(phrase.index("M")) # 6
print(phrase.index("l")) # 2
print(phrase.replace("H", "h")) # hello Mr.White