"""yib sai klong"""
W, L, M, N = map(int, input().split())
MIN = W * L

for i in range(M , N + 1):
    used1 = W * (L // i) * i
    used2 = (L % i) * (W // i) * i
    waste = (W * L) - (used1 + used2)

    if waste < MIN:
        MIN = waste

print(MIN)
