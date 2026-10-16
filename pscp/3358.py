"""Pig"""
n = int(input())
weights = list(map(int, input().split()))

max_list = []

for i in range(n):
    w1 = weights[i * 2]
    w2 = weights[i * 2 + 1]

    if w1 > w2:
        max_list.append(w1)
    else:
        max_list.append(w2)

if n == 1:
    print(max_list[0])
else:
    print(" + ".join(map(str, max_list)), "=", sum(max_list))
