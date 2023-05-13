import random

# 1.號碼不能重複
# 2.要排序

numbers = []
# 使用無窮迴圈
while True:
    x = random.randint(1, 49)
    # 不存在的號碼才加入
    if x not in numbers:
        numbers.append(x)
    # 跳離無窮迴圈
    if len(numbers) == 6:
        break

# 增加排序功能(sorted)
print(sorted(numbers), end=" ")

y = random.randint(1, 49)
print(f"特別號:{y}")
