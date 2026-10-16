"""cave"""
n = int(input())
cave = list(map(int, input().split()))
cmd = input().strip()

pos = -1
chest = -1
for i in range(n):
    if cave[i] == 1:
        pos = i
    if cave[i] == 2:
        chest = i

cave[pos] = 0

found_chest = False
for c in cmd:
    if not found_chest:
        if c == 'L' and pos > 0:
            pos = pos - 1
        elif c == 'R' and pos < n - 1:
            pos = pos + 1

        if pos == chest:
            found_chest = True

cave[pos] = 1

for i in range(n):
    if i == n - 1:
        print(cave[i])
    else:
        print(cave[i], end=" ")
