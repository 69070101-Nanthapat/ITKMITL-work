"""Promotion"""
buy = input().split()
a = int(buy[0])
b = int(buy[1])
c = int(buy[2])
total = 0

item = a + b + c
if item >= 3:
    total = ((a * 25) + (b * 40) + (c * 55))*0.9
    print(int(total))
else:
    total = (a * 25) + (b * 40) + (c * 55)
    print(int(total))
