# 列表list 列表的用法
scores = [90, 70, 60, 60, 80]
friends = ["Harry", "Ron", "Hermione"]
# print(friends)
things = [90, "小灰", True]
# print(things)


# print(scores)
# print(scores[0]) # 90
# print(scores[3]) # 50
# print(scores[-1]) # 80
# print(scores[-2]) # 50
# print(scores[0:2]) # [90, 70] 從第0位開始取到第2位之前
# print(scores[1:4]) # [70, 60, 50] 從第1位開始取到第4位之前
# print(scores[1:]) # [70, 60, 50, 80] 從第0位開始取到最後
# print(scores[:4]) # [90, 70, 60, 50] 取第4位以前

phrase = "Hello Mr.White"
# print(phrase[0:5]) # Hello
# print(phrase[6:]) # Mr.White

# scores[0] = 30
# print(scores) # [30, 70, 60, 50, 80]

# scores.extend(friends) # 在list延伸另一個list
# print(scores) # [30, 70, 60, 50, 80, 'Harry', 'Ron', 'Hermione']

# scores.append(30) # 在list後面加上一個值
# print(scores) # [90, 70, 60, 50, 80, 30] 

# scores.insert(2, 40) # 在第2位插入40
# print(scores) # [90, 70, 40, 60, 50, 80]

# scores.remove(70) # 移除70
# print(scores) # [90, 60, 50, 80]

# scores.clear() # 清空list
# print(scores) # []

# scores.pop() # 移除最後一位
# print(scores) # [90, 70, 60, 50]

# scores.sort() # 由小到大排列
# print(scores) # [50, 60, 70, 80, 90]

# scores.reverse() # 反轉list
# print(scores) # [80, 50, 60, 70, 90]

# print(scores.index(90)) # 0
# print(scores.index(60)) # 2 回傳第一個找到的位置

print(scores.count(60)) # 2 計算有幾個
print(scores.count(80)) # 1
print(scores.count(100)) # 0