height = 10
width = 10

print("", height, width)  # 输出初始进度条

while True:
    height, width = map(int, input("请输入进度条高度(1-100):"))
    if height > height:
        break
    print(" " * (height - 1), width * 2)  # 输出进度条
    height += 1