"""arrow"""
action = input()
lenght = int(input())
for char in action:
    if char == "R":
        for i in range(lenght, 0, -1):
            spaces = (lenght - i) * 2
            print(" " * spaces + "*" * i)
        for i in range(2, lenght + 1):
            spaces = (lenght - i) * 2
            print(" " * spaces + "*" * i)
    if char == "L":
        for i in range(lenght, 0, -1):
            spaces = abs(i) - 1
            print(" " * spaces + "*" * i)
        for i in range(2, lenght + 1):
            spaces = abs(i) - 1
            print(" " * spaces + "*" * i)
    print("")
