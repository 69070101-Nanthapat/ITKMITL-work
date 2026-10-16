"""แลกเหรียญ"""
cash = int(input())
tencoin = cash // 10
cash = cash % 10
fivecoin = cash // 5
cash = cash % 5
two = cash // 2
cash = cash % 2
coin = cash

print(f"10 = {tencoin}")
print(f"5 = {fivecoin}")
print(f"2 = {two}")
print(f"1 = {coin}")
