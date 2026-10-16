"""RAMEN"""
line1 = input().split()
size = line1[0]
genre = line1[1]
line2 = input().split()
topping = line2[0]
if topping == "N":
    AMOUNT = 0
else:
    AMOUNT = int(line2[1])

if size == "S" and genre == "R":
    if topping == "N":
        print("60")
    elif topping == "P":
        print(60+(15*AMOUNT))
    elif topping == "E":
        print(60+(10*AMOUNT))
elif size == "S" and genre == "T":
    if topping == "N":
        print("80")
    elif topping == "P":
        print(80+(15*AMOUNT))
    elif topping == "E":
        print(80+(10*AMOUNT))
elif size == "M" and genre == "R":
    if topping == "N":
        print("80")
    elif topping == "P":
        print(80+(15*AMOUNT))
    elif topping == "E":
        print(80+(10*AMOUNT))
elif size == "M" and genre == "T":
    if topping == "N":
        print("100")
    elif topping == "P":
        print(100+(15*AMOUNT))
    elif topping == "E":
        print(100+(10*AMOUNT))
elif size == "L" and genre == "R":
    if topping == "N":
        print("100")
    elif topping == "P":
        print(100+(15*AMOUNT))
    elif topping == "E":
        print(100+(10*AMOUNT))
elif size == "L" and genre == "T":
    if topping == "N":
        print("120")
    elif topping == "P":
        print(120+(15*AMOUNT))
    elif topping == "E":
        print(120+(10*AMOUNT))
