"""christmas"""
x = input().split()
color = x[0]
count = int(x[1])
led = ""

for _ in range(count):
    if color == "R":
        led += "Red "
        color = "G"
    elif color == "G":
        led += "Green "
        color = "B"
    else:
        led += "Blue "
        color = "R"

print(led)
