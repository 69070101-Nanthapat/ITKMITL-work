"""pass/not pass"""
midterm = int(input())
final = int(input())
total = midterm + final
if total >= 50:
    print(total)
    print("pass")
else:
    print(total)
    print("fail")
