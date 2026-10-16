"""1234"""
def main():
    """1234"""
    power = int(input())
    result = 0
    pattern = power % 4
    if power == 0:
        result = 1
    elif pattern == 1:
        result = 7
    elif pattern == 2:
        result = 9
    elif pattern == 3:
        result = 3
    elif pattern == 0:
        result = 1
    print(result)

main()
