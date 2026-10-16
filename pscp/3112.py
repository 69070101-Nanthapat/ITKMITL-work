"""BOBA"""
line1 = input().split()
boba_type = line1[0]
boba = float(line1[1])
boba_energy = 0

line2 = input().split()
tea_type = line2[0]
level = int(line2[1])
tea = int(line2[2])
tea_energy = 0

if boba_type == "H":
    boba_energy = 5*boba
elif boba_type == "O":
    boba_energy = 3*boba
else:
    boba_energy = 2*boba

if tea_type == "R":
    if level == 1:
        tea_energy = 12*tea
    elif level == 2:
        tea_energy = 18*tea
    elif level == 3:
        tea_energy = 25*tea
elif tea_type == "T":
    if level == 1:
        tea_energy = 15*tea
    elif level == 2:
        tea_energy = 20*tea
    elif level == 3:
        tea_energy = 30*tea
elif tea_type == "M":
    if level == 1:
        tea_energy = 10*tea
    elif level == 2:
        tea_energy = 15*tea
    elif level == 3:
        tea_energy = 20*tea
if boba_energy.is_integer():
    print(int(boba_energy+tea_energy))
else:
    print(boba_energy+tea_energy)
