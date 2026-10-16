"""easy histrogram"""
s = input()

order = []
for i in range(26):
    order.append(chr(97 + i))
    order.append(chr(65 + i))

for c in order:
    cnt = s.count(c)
    if cnt > 0:
        print(f"{c} = {cnt}")
