"""min"""
x = int(input())
for i in range(x):
    num = int(input())
    if not i:
        min_num = num
    elif num < min_num:
        min_num = num
print(min_num)
