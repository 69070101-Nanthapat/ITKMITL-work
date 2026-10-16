"""demon slayer"""

queue = [
    ("Spider Demon", 1),
    ("Swamp Demon", 2),
    ("Arrow Demon", 1),
    ("Hand Demon", 2),
    ("Drum Demon", 3),
    ("Mugen Train", 2),
    ("Upper Moon", 3)
]

kills = 0
total_attacks = 0

while kills < 5:
    name, correct = queue.pop(0)
    print(name)

    att = 0
    passed = False
    while att < 2:
        try:
            val = int(input().strip())
        except EOFError:
            break
        total_attacks += 1
        att += 1

        if val == correct:
            print("kill")
            kills += 1
            passed = True
            break

    if passed:
        if kills == 5:
            break
    else:
        print("back")
        queue.append((name, correct))

print(total_attacks)
