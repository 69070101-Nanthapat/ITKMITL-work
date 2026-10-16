"""Taxi"""
distance = int(input())
if distance <= 0:
    print("0")
elif distance <= 1:
    print("35")
elif 1 < distance <= 10:
    print(35+(distance-1)*5)
elif distance > 10:
    print(35+(10-1)*5+(distance-10)*8)
