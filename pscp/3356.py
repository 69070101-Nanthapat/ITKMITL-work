"""Bus seat"""
r = int(input())
n = int(input())
k = int(input())

i = 1
while i <= r:
    j = 1
    s = ""
    while j <= n:
        seat = (j - 1) * r + (r - i + 1)
        if seat == k:
            v = "XX"
        elif seat < 10:
            v = "0" + str(seat)
        else:
            v = str(seat)
        
        if s == "":
            s = v
        else:
            s += " " + v
        j += 1
    print(s)
    if i == r // 2:
        print()
    i += 1
