"""sell car"""
n = int(input())
x = []
i = 0
while i < n:
    eff = input().split()[1]
    x.append(int(eff))
    i += 1

ans = 0
mx = -1
i = n - 1
while i >= 0:
    if x[i] < mx:
        ans += 1
    else:
        mx = x[i]
    i -= 1

print(ans)
