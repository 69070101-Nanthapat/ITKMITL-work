"""BONUS"""
position , years_str, salary_str = input().split()
years = float(years_str)
salary = float(salary_str)

bonus = 0
rate = 0.0

if position == "M":
    bonus = 1500
    if years <= 5:
        rate = 0.06
    elif years <= 10:
        rate = 0.08
    else:
        rate = 0.10

elif position == "B":
    bonus = 1000
    if years <= 5:
        rate = 0.05
    elif years <= 10:
        rate = 0.06
    else:
        rate = 0.07

elif position == 'G':
    bonus = 500
    if years <= 5:
        rate = 0.04
    elif years <= 10:
        rate = 0.05
    else:
        rate = 0.06
total = bonus + (salary * rate)
print(int(total))
