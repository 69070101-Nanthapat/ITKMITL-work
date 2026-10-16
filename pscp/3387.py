"""tuple"""
line1 = input().split()
data = tuple(line1)
target = input().strip()

idx = data.index(target)
size = data.count(target)

ROW = " ".join([str(idx)] * size)
for _ in range(size):
    print(ROW)
