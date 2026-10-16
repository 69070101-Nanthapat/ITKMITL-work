"""1234"""
def main():
    """1234"""
    num = int(input())
    press = 0
    for i in range(1,num+1):
        press += len(str(i))

    if num == 1:
        print(1)
    else:
        print(num+press)

main()
