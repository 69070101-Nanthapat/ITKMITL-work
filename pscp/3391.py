"""magic coin collection"""
N = int(input())

total_fire = 0
total_water = 0
total_earth = 0

for _ in range(N):
    f1, w1, e1, f2, w2, e2 = map(int, input().split())

    total_fire += max(f1, f2)
    total_water += max(w1, w2)
    total_earth += max(e1, e2)

total_score = total_fire + total_water + total_earth

BONUS = "YES" if total_fire > (total_water + total_earth) else "NO"

print(f"Total: {total_score}")
print(f"Fire: {total_fire}")
print(f"Water: {total_water}")
print(f"Earth: {total_earth}")
print(f"Bonus: {BONUS}")
