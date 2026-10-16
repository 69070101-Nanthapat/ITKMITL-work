"""array"""
nums = []
for i in range(1, 4):
    val = int(input())
    nums.append(val)
    print(f"Input number {i} stored.")

while True:
    menu = int(input())

    if not menu:
        break
    if menu == 1:
        RES = " ".join(map(str, nums))
        print(f"Original order: {RES}")
    elif menu == 2:
        desc = sorted(nums, reverse=True)
        RES = " ".join(map(str, desc))
        print(f"Descending order: {RES}")
    elif menu == 3:
        asc = sorted(nums)
        RES = " ".join(map(str, asc))
        print(f"Ascending order: {RES}")
