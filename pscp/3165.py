"""walking"""
text = input()
x = 0
y = 0
for char in text:
    if char == "N":
        y += 1
    elif char == "S":
        y -= 1
    elif char == "E":
        x += 1
    elif char == "W":
        x -= 1
d = abs(x) + abs(y)
print(x, y, d)
