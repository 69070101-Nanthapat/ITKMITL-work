"""RectangleArea overlapping"""
first = input().split()
second = input().split()
x1 = int(first[0])
y1 = int(first[1])
width1 = int(first[2])
height1 = int(first[3])
x2 = int(second[0])
y2 = int(second[1])
width2 = int(second[2])
height2 = int(second[3])

if x1 + width1 <= x2 or x1 >= x2 + width2 or y1 + height1 <= y2 or y1 >= y2 + height2:
    print("no overlapping")
else:
    left = x1 if x1 > x2 else x2
    right = x1 + width1 if x1 + width1 < x2 + width2 else x2 + width2
    bottom = y1 if y1 > y2 else y2
    top = y1 + height1 if y1 + height1 < y2 + height2 else y2 + height2
    print((right - left) * (top - bottom))
