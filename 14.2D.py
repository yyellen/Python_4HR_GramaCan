# 二維列表、巢狀迴圈
# row = 行
# column = 列

nums = [
    [0,1,2], 
    [3,4,5], 
    [6,7,8], 
    [9]
]

# print(nums[0][0]) # 0
# print(nums[1][2]) # 5
# print(nums[3][0]) # 9


for row in nums:
    for col in row:
        print(col)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9