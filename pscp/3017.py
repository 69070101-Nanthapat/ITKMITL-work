"""12345"""
def main():
    """asdfeasf"""
    price = float(input())
    if price * 10 / 100 > 1000:
        price = price + 1000
    elif price * 10 / 100 > 50:
        price = price + (price * 10 / 100)
    else:
        price = price + 50
    total = price * 1.07
    print(f"{total:.2f}")

main()
