"""iint"""
op1, num_nuay = input().split()
op2, num_sib = input().split()
op3, num_roi = input().split()


num_nuay = int(num_nuay)
num_sib = int(num_sib)
num_roi = int(num_roi)

for i in range(10):
    roi = False
    if op3 == "==" and i == num_roi:
        roi = True
    elif op3 == ">"  and i > num_roi:
        roi = True
    elif op3 == "<"  and i < num_roi:
        roi = True
    elif op3 == ">=" and i >= num_roi:
        roi = True
    elif op3 == "<=" and i <= num_roi:
        roi = True
    elif op3 == "!=" and i != num_roi:
        roi = True

    if roi:
        for j in range(10):
            sib = False
            if op2 == "==" and j == num_sib:
                sib = True
            elif op2 == ">"  and j > num_sib:
                sib = True
            elif op2 == "<"  and j < num_sib:
                sib = True
            elif op2 == ">=" and j >= num_sib:
                sib = True
            elif op2 == "<=" and j <= num_sib:
                sib = True
            elif op2 == "!=" and j != num_sib:
                sib = True

            if sib:
                for k in range(10):
                    nuay = False
                    if op1 == "==" and k == num_nuay:
                        nuay = True
                    elif op1 == ">"  and k > num_nuay:
                        nuay = True
                    elif op1 == "<"  and k < num_nuay:
                        nuay = True
                    elif op1 == ">=" and k >= num_nuay:
                        nuay = True
                    elif op1 == "<=" and k <= num_nuay:
                        nuay = True
                    elif op1 == "!=" and k != num_nuay:
                        nuay = True

                    if nuay:
                        print(f"{i}{j}{k}")
