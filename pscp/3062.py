"""ticket"""
age = int(input())
state = input().lower()
if age < 18 or state == "s":
    print("20")
else:
    print("50")
