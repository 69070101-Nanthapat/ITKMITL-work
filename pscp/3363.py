"""Rabbit flu"""

row_input = input().split()
R = int(row_input[0])
C = int(row_input[1])

rabbit_input = input().split()
r = int(rabbit_input[0])
c = int(rabbit_input[1])

N = int(input())

infected_list = []
i = 0
while i < N:
    inf_input = input().split()
    infected_list.append((int(inf_input[0]), int(inf_input[1])))
    i += 1

grid = [[0] * C for _ in range(R)]

for inf_r, inf_c in infected_list:
    i = 0
    while i < R:
        j = 0
        while j < C:
            dr = abs(i - inf_r)
            dc = abs(j - inf_c)
            k = dr if dr > dc else dc

            risk = 0
            if not k:
                risk = 100
            elif k == 1:
                risk = 60
            elif k == 2:
                risk = 20

            if risk > grid[i][j]:
                grid[i][j] = risk
            j += 1
        i += 1

safe_zone_count = 0
i = 0
while i < R:
    j = 0
    while j < C:
        if not grid[i][j]:
            safe_zone_count += 1
        j += 1
    i += 1

print(safe_zone_count)
print(str(grid[r][c]) + "%")
