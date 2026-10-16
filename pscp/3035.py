"""AR tiktok"""
info = input().split(" ")
r = int(info[0])
x = int(info[1])
y = int(info[2])
if (x**2 + y**2) < r**2:
    print("IN")
elif (x**2 + y**2) == r**2:
    print("ON")
else:
    print("OUT")
