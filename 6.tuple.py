# 元祖 tuple 創建後不能新增, 修改, 刪除，存放不希望變更的資料
scores = (90, 80, 70, 50)

print(scores[0]) # 90
print(scores[0:2]) # (90, 80)
print(len(scores)) # 4 取得長度

scores[0] = 30
print(scores) # TypeError: 'tuple' object does not support item assignment