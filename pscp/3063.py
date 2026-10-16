"""password"""
CHAR = "H"
DIGIT = "4567"
char_input = input()
digit_input = input()
if char_input == CHAR and digit_input == DIGIT:
    print("safe unlocked")
elif char_input != CHAR and digit_input == DIGIT:
    print("safe locked - change char")
elif char_input == CHAR and digit_input != DIGIT:
    print("safe locked - change digit")
else:
    print("safe locked")
