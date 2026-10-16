"""even odd"""
first = int(input())
second = int(input())
third = int(input())
even = 0
odd = 0
if not first % 2:
    even += 1
else:
    odd += 1
if not second % 2:
    even += 1
else:
    odd += 1
if not third % 2:
    even += 1
else:
    odd += 1
print(even)
print(odd)
