"""gong charm"""
n = int(input())
counts = {}

for _ in range(n):
    size = input()
    if size in counts:
        counts[size] += 1
    else:
        counts[size] = 1

print(max(counts.values()))
