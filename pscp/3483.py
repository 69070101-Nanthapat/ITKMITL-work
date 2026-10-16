"""ma pen team"""
N, M = map(int, input().split())

if N < 1 or N > 10 or M < 1 or M > 20:
    print("Data Incorrect")
else:
    grid = []
    invalid = False

    for i in range(N):
        row = list(map(int, input().split()))
        grid.append(row)

        for score in row:
            if score < 0 or score > 100:
                invalid = True

    if invalid:
        print("Data Incorrect")
    else:
        total_all = 0

        for i in range(N):
            team_sum = sum(grid[i])
            avg = team_sum / M
            mx = max(grid[i])

            total_all += team_sum

            print(f"Team {i + 1}: Average = {avg:.2f}, Max = {mx}")

        print(f"Total Score of All Teams = {total_all}")
