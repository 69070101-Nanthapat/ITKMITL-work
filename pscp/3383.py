"""Difference"""
n = int(input())
m = int(input())

set_a = set()
for _ in range(n):
    set_a.add(int(input()))

set_b = set()
for _ in range(m):
    set_b.add(int(input()))

result_set = set_a - set_b

for x in sorted(result_set):
    print(x, end=' ')
