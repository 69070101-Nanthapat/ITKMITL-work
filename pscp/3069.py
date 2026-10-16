"""zodiac"""
date = int(input())
month = int(input())
if (22 <= date <= 31 and month == 12) or (1 <= date <= 19 and month == 1):
    print("capricorn")
elif (20 <= date <= 31 and month == 1) or (1 <= date <= 18 and month == 2):
    print("aquarius")
elif (19 <= date <= 29 and month == 2) or (1 <= date <= 20 and month == 3):
    print("pisces")
elif (21 <= date <= 31 and month == 3) or (1 <= date <= 19 and month == 4):
    print("aries")
elif (20 <= date <= 30 and month == 4) or (1 <= date <= 20 and month == 5):
    print("taurus")
elif (21 <= date <= 31 and month == 5) or (1 <= date <= 21 and month == 6):
    print("gemini")
elif (22 <= date <= 30 and month == 6) or (1 <= date <= 22 and month == 7):
    print("cancer")
elif (23 <= date <= 31 and month == 7) or (1 <= date <= 22 and month == 8):
    print("leo")
elif (23 <= date <= 31 and month == 8) or (1 <= date <= 22 and month == 9):
    print("virgo")
elif (23 <= date <= 30 and month == 9) or (1 <= date <= 23 and month == 10):
    print("libra")
elif (24 <= date <= 31 and month == 10) or (1 <= date <= 21 and month == 11):
    print("scorpio")
elif (22 <= date <= 30 and month == 11) or (1 <= date <= 21 and month == 12):
    print("sagittarius")
