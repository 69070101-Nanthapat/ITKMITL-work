"""smart trash collector"""

n = int(input())

for _ in range(n):
    p = input().split()
    w1, w2, w3 = float(p[0]), float(p[1]), float(p[2])

    tot = w1 + w2 + w3
    res = f"{tot:.1f}"

    msg = []
    if tot > 50.0:
        msg.append("Overloaded")

    if w1 > 20.0:
        msg.append("Check Type Plastic")
    if w2 > 20.0:
        msg.append("Check Type Can")
    if w3 > 20.0:
        msg.append("Check Type Glass")

    if msg:
        res += ", " + ", ".join(msg)

    print(res)
