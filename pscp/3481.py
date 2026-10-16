"""bridge"""
N = int(input().split()[1])

bridges = []
for _ in range(N):
    a, b = map(int, input().split())
    bridges.append((a, b))

max_bridges = 0

for a, b in bridges:
    x = a + 0.5

    count = 0
    for start, end in bridges:
        if start < x < end:
            count += 1

    if count > max_bridges:
        max_bridges = count

print(max_bridges)
