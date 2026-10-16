"""increase decrease"""
first = float(input())
second = float(input())
third = float(input())
if first < second < third:
    print("increasing")
elif first > second > third:
    print("decreasing")
else:
    print("neither")
