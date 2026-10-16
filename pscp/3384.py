"""pick them"""
import json
data = json.loads(input())

even = False

for x in data:
    if not x % 2:
        print(x)
        even = True

if not even:
    print("Nope")
