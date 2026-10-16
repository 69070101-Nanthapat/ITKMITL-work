"""electric using"""
N = int(input())
base = 0
if N <= 10:
    base = N * 5
elif N <= 50:
    base = (10 * 5) + (N - 10) * 7
elif N <= 100:
    base = (10 * 5) + (40 * 7) + (N - 50) * 10
elif N <= 200:
    base = (10 * 5) + (40 * 7) + (50 * 10) + (N - 100) * 12
else:
    base = (10 * 5) + (40 * 7) + (50 * 10) + (100 * 12) + (N - 200) * 15

vat = base * 0.07
ft = N * 0.50
total = base + vat + ft
final = int(total * 10 + 0.5) / 10
print(f"{final:.1f}")
