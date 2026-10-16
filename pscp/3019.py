"""1234"""
def main():
    """1234"""
    safechar = "H"
    safedigit = "4567"
    char = input()
    digit = input()
    if char == safechar and digit == safedigit:
        print("safe unlocked")
    elif char != safechar and digit == safedigit:
        print("safe locked - change char")
    elif char == safechar and digit != safedigit:
        print("safe locked - change digit")
    else:
        print("safe locked")
main()
