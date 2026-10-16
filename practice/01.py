"""char type"""
x = input()
upper = 0
lower = 0
number = 0
for char in x:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char.isdigit():
        number += 1
print(upper, lower, number)
