"""12345"""
def main():
    """asdfeasf"""
    RA = int(input())
    RB = int(input())
    String = input()
    Ea = 1 / (1+10**((RB-RA)/400))
    Eb = 1 / (1+10**((RA-RB)/400))
    if String == "A":
        print(f"{Ea:.2f}")
    else:
        print(f"{Eb:.2f}")

main()
