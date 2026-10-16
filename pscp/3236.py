"""rahus fad take"""
n = int(input())
id1 = input()
id2 = input()
not_match = 0

for i in range(n):
    if int(id1[i])+int(id2[i]) != 9:
        not_match += 1

if not not_match:
    print("YES")
else:
    print(f"NO {not_match}")
