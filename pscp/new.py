"""hotel 13"""
x = input()
x1 = int(x[0])
x2 = int(x[1])
x3 = int(x[2])
x4 = int(x[3])
x5 = int(x[4])
back = x[::-1]
sumx = int(x1 + x2 + x3 + x4 + x5)
powerx = int(x1 * x2 * x3 * x4 * x5)

first = ""
second = ""
third = ""

if x1 > 5:
    first = "9"
elif x2 > 5:
    first = "10"
elif x3 > 5:
    first = "11"
elif x4 > 5:
    first = "12"
elif x5 > 5:
    first = "14"
else:
    first = "13"

if x == back:
    if x1 + x5 > 5:
        second = "1"
    elif x2 * x4 > 5:
        second = "2"
    else:
        second = "0"
else:
    if x1 and x5 // x5 > 5:
        second = "1"
    elif x2-x5 > 5:
        second = "2"
    else:
        second = "0"


if sumx > 25:
    third = "1"
elif powerx > 55:
    third = "2"
else:
    third = "0"

print(f"{first}{second}{third}")
