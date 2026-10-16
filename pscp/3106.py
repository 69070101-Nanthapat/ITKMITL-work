"""bank clash"""
money = int(input())

if money < 100 or money > 20000 or money % 100:
    print("ERROR")
else:
    pun = money // 1000
    money %= 1000
    haroi = money // 500
    money %= 500
    roi = money // 100
    if pun > 0 and haroi > 0 and roi > 0:
        print(f"1000 = {pun}")
        print(f"500 = {haroi}")
        print(f"100 = {roi}")
    elif pun > 0 and haroi > 0 and not roi:
        print(f"1000 = {pun}")
        print(f"500 = {haroi}")
    elif pun > 0 and not haroi and roi > 0:
        print(f"1000 = {pun}")
        print(f"100 = {roi}")
    elif not pun and haroi > 0 and roi > 0:
        print(f"500 = {haroi}")
        print(f"100 = {roi}")
    elif pun > 0 and not haroi and not roi:
        print(f"1000 = {pun}")
    elif not pun and haroi > 0 and not roi:
        print(f"500 = {haroi}")
    elif not pun and not haroi and roi > 0:
        print(f"100 = {roi}")
