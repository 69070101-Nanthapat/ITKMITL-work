"""kao taw"""
n = int(input().split()[0])
h = list(map(int, input().split()))
customers = list(map(int, input().split()))

max_before = [0] * n
cur_max = 0
for i in range(n):
    max_before[i] = cur_max
    if h[i] > cur_max:
        cur_max = h[i]

for idx in customers:
    pos = idx - 1
    m = max_before[pos]

    need = (m + 1) - h[pos]
    if need < 0:
        need = 0

    print(need)
