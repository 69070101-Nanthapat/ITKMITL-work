"""temperature"""
n = int(input())
temp = input().split()
count = 0
total = 0
for i in range(n):
    total += int(temp[i])
avg = total / n

for i in range(n):
    if int(temp[i]) > avg:
        count += 1

print(f"{avg:.2f}")
print(count)
