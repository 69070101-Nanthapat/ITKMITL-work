"""total + max"""
num = int(input())
total = 0
most = []
for _ in range(num):
    x = int(input())
    y = int(input())
    if x > y:
        total += x
        most.append(str(x))
    else:
        total += y
        most.append(str(y))
if num == 1:
    if x > y:
        print(x)
    else:
        print(y)
else:
    TEXT = " + ".join(most)
    print(f"{TEXT} = {total}")
