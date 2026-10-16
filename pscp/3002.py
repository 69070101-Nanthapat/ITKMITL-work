"""12345"""
def main():
    """asdfeasf"""
    name = input()
    surname = input()
    age = input()
    if len(name) >= 5 and len(surname) >= 5:
        print(f"{name[0:2]}{surname[-1]}{age[-1]}")
    else:
        print(f"{name[0]}{age}{surname[-1]}")

main()
