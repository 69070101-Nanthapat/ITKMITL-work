"""Buppaesanniwaz"""
a = input().strip()
b = input().strip()

i = 0
while len(a) < len(b):
    a += a[i]
    i += 1

i = 0
while len(b) < len(a):
    b += b[i]
    i += 1

r = ""
w_count = 0

for i in range(len(a)):
    c1 = a[i].lower()
    c2 = b[i].lower()
    if c1 in "love" or c2 in "love":
        r += "w"
        w_count += 1
    else:
        r += "$"

if w_count % 2:
    max_consecutive = 0
    current_consecutive = 0
    for char in r:
        if char == "w":
            current_consecutive += 1
            if current_consecutive > max_consecutive:
                max_consecutive = current_consecutive
        else:
            current_consecutive = 0
    r += str(max_consecutive)
else:
    has_consecutive_w = False
    for i in range(len(r) - 1):
        if r[i] == "w" and r[i + 1] == "w":
            has_consecutive_w = True
            break

    if not has_consecutive_w:
        r += "#"

print(r)
