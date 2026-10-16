"""sang rob"""
n, k = map(int, input().split())

s = []
for _ in range(n):
    s.append(int(input()))

min_s = s[0]
for t in s:
    if t < min_s:
        min_s = t

winner_time = k * min_s

survivors = 0
for t in s:

    if (k - 1) * t < winner_time:
        survivors += 1

print(survivors)
