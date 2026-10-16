"""som dul she wit"""
n = int(input())
x = []
less = []
more = []

for _ in range(n):
    num = int(input())
    x.append(num)

for word in x:
    if word <= 18:
        less.append(word)
    else:
        more.append(word)
print(n + max(0, len(more) - len(less) - 1))
