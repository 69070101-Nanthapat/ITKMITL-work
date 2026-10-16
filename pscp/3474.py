""" Resistor """
digit = {
    "Black": 0, "Brown": 1, "Red": 2, "Orange": 3, "Yellow": 4,
    "Green": 5, "Blue": 6, "Purple": 7, "Grey": 8, "White": 9,
}
mult = {
    "Black": 1, "Brown": 10, "Red": 100, "Orange": 1000,
    "Yellow": 10000, "Green": 100000, "Blue": 1000000,
    "Purple": 10000000, "Gold": 0.1, "Silver": 0.01,
}
tol = {
    "Brown": 1, "Red": 2, "Green": 0.5, "Blue": 0.25,
    "Purple": 0.10, "Grey": 0.05, "Gold": 5, "Silver": 10,
}

a = input().strip()
b = input().strip()
c = input().strip()
d = input().strip()

if a not in digit or b not in digit or c not in mult or d not in tol:
    print("Error")
else:
    value = (digit[a] * 10 + digit[b]) * mult[c]
    p = tol[d]
    low = value * (1 - p / 100)
    high = value * (1 + p / 100)
    print(f"{low:.4f}")
    print(f"{high:.4f}")
