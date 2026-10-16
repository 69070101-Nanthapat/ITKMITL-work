"""bird"""
n = int(input())
h = list(map(int, input().split()))

ans = 0

for i in range(n):
    left_ok = (not i) or (h[i] > h[i - 1])
    right_ok = (i == n - 1) or (h[i] > h[i + 1])

    if left_ok and right_ok:
        ans += 1

print(ans)
