# 檔案的讀取、寫入

# open("檔案路徑", mode="開啟模式")
# 絕對路徑 C:/Users/ytwang/OneDrive - 遠見天下文化出版股份有限公司/桌面/Python/123.txt 斜線要反過來，不然執行會有問題
# 相對路徑 以程式的位置做延伸 ex: 123.txt

# mode="r" 讀取
# mode="w" 覆寫
# mode="a" 在原先的資料後寫東西


file = open("123.txt", mode="r")
print(file.read())
print(file.readline()) # 只讀第一行

# 一行一行讀出來
for line in file:
    print(line)

print(file.readlines()) # 把每一行資料放進一個列表

file.close() # 記得關閉檔案才不會占用資源


file = open("123.txt", mode="w")
file.write("hi")
file.close()

file = open("123.txt", mode="a", encoding="utf-8")
# file.write(" world")
file.write("\n你好")
file.close()

# 用with省去.close()
with open("123.txt", mode="a", encoding="utf-8") as file:
    file.write("\n哈哈")